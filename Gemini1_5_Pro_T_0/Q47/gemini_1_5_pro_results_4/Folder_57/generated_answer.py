def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 94 + 1):
        for j in range(i, 94 + 1):
            substring = text[i:j + 1]
            if 39 <= len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes