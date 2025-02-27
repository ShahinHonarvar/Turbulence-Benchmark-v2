def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 98):
        for j in range(i + 9, min(98, i + 36)):
            substring = text[i:j + 1]
            if len(substring) >= 10 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes