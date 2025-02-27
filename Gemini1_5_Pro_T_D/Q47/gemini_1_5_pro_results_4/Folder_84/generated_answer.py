def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(23, 78):
        for j in range(i, 78):
            substring = text[i:j + 1].lower()
            if 13 <= len(substring) <= 40 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes