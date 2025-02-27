def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i, 93):
            substring = text[i:j + 1]
            if 17 <= len(substring) <= 66 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes