def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 84 + 1):
        for j in range(i, 84 + 1):
            substring = text[i:j + 1]
            if len(substring) >= 21 and len(substring) <= 31 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes