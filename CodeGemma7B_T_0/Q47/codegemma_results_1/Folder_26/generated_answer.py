def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(24, 85):
        for j in range(i - 20, i + 1):
            if j < 0 or j >= len(text):
                continue
            if text[i] == text[j]:
                palindrome = text[j:i + 1]
                if len(palindrome) >= 21 and len(palindrome) <= 31:
                    palindromes.add(palindrome)
    return palindromes