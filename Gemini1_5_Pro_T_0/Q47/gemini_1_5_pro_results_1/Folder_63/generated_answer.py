def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i + 25, min(86, i + 31) + 1):
            substring = text[i:j]
            if len(substring) >= 26 and len(substring) <= 31 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes