def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 75):
        for j in range(i, 75):
            substring = text[i:j]
            if 23 <= len(substring) <= 39 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes