def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 98):
        for j in range(i, 98):
            substring = text[i:j + 1]
            if 10 <= len(substring) <= 36 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes