def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(43, 96):
        for j in range(i, 96):
            substring = text[i:j + 1]
            if 18 <= len(substring) <= 47 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes