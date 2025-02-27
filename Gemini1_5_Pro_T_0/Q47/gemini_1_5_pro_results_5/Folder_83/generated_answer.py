def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(75, 96):
        for j in range(i, 96):
            substring = text[i:j + 1]
            if 7 <= len(substring) <= 9 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes