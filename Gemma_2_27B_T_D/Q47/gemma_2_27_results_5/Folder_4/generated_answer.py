def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i, min(i + 66, 93)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1] and (17 <= len(substring) <= 66):
                palindromes.add(substring)
    return palindromes