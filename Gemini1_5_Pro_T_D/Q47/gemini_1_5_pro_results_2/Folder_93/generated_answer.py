def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 96):
        for j in range(i, 96):
            substring = text[i:j + 1]
            if 13 <= len(substring) <= 49 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes