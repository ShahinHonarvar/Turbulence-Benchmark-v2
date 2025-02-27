def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i, 296):
            substring = text[i:j + 1]
            if 136 <= len(substring) <= 160 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes