def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 75):
        for j in range(i, 75):
            substring = text[i:j + 1]
            if len(substring) >= 6 and len(substring) <= 8 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes