def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(34, 91):
        for j in range(i - 13, i + 20):
            if j >= len(text) or j < 0:
                continue
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if len(palindrome) >= 14 and len(palindrome) <= 39:
                    palindromes.add(palindrome)
    return palindromes