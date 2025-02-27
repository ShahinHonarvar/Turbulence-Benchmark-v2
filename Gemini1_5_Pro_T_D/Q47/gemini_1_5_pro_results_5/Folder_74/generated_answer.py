def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(30, 85):
        for j in range(i, 85):
            substring = text[i:j + 1]
            if 12 <= len(substring) <= 20 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes