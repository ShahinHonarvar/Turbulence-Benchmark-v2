def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i, min(i + 66, 93)):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha() and (17 <= len(substring) <= 66):
                palindromes.add(substring)
    return palindromes