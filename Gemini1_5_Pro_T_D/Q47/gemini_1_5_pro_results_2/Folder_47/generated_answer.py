def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(39, 95):
        for j in range(i, 95):
            substring = text[i:j + 1]
            if 14 <= len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes