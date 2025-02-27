def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 80):
        for j in range(i, 80):
            substring = text[i:j + 1]
            if 35 <= len(substring) <= 41 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes