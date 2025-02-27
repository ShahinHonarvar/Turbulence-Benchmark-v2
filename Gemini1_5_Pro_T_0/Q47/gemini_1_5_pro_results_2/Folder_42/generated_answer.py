def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(43, 96):
        for j in range(i, 96):
            substring = text[i:j + 1]
            if 18 <= len(substring) <= 47 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes