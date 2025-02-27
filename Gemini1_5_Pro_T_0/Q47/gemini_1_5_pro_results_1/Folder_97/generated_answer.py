def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(28, 95):
        for j in range(i, 95):
            substring = text[i:j]
            if 38 <= len(substring) <= 49 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes