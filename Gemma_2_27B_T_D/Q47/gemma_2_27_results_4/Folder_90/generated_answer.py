def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 281):
        for j in range(i, 281):
            substring = text[i:j + 1]
            if len(substring) >= 136 and len(substring) <= 151 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes