def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 123):
        for j in range(i, min(123, i + 221 // 2)):
            substring = text[i:j + 1]
            if len(substring) >= 12 and len(substring) <= 220 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes