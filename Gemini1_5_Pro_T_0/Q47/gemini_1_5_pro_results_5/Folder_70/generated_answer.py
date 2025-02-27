def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 71):
        for j in range(i, 71):
            substring = text[i:j + 1]
            if 24 <= len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes