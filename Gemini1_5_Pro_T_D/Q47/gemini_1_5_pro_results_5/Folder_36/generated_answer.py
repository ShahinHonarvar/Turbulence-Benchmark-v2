def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 283 - 115 + 2):
        for j in range(i + 115 - 1, min(283 + 1, i + 134)):
            substring = text[i:j + 1]
            if len(substring) >= 115 and len(substring) <= 134 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes