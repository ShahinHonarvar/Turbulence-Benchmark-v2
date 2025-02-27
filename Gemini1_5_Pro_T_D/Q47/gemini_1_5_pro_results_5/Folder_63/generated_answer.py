def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 85 - 25):
        for j in range(i + 25, 86):
            substring = text[i:j + 1]
            if len(substring) >= 26 and len(substring) <= 31 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes