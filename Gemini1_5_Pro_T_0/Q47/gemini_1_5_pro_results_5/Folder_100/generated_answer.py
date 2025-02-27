def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 97):
        for j in range(i, 97):
            substring = text[i:j + 1]
            if 12 <= len(substring) <= 18 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes