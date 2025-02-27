def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 91):
        for j in range(i, 91):
            substring = text[i:j + 1]
            if 27 <= len(substring) <= 58 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes