def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 77):
        for j in range(i, 78):
            substring = text[i:j + 1]
            if 13 <= len(substring) <= 40 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes