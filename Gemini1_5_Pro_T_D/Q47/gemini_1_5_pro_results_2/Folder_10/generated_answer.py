def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 61):
        for j in range(i, 61):
            substring = text[i:j + 1]
            if 16 <= len(substring) <= 39 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes