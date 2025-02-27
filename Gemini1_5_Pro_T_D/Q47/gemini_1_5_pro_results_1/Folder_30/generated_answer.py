def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(14, 91):
        for j in range(i, 91):
            substring = text[i:j + 1]
            if 55 <= len(substring) <= 71 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes