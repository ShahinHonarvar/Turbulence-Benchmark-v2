def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(200, 301):
        for j in range(i - 9, i + 1):
            if j < 0 or j >= len(text):
                continue
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if len(palindrome) >= 10 and len(palindrome) <= 50:
                    palindromes.add(palindrome)
    return palindromes