def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i, 60):
            substring = text[i:j + 1]
            if 18 <= len(substring) <= 36 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes