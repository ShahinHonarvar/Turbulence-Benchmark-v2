def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(43, 95 - 18 + 2):
        for j in range(i + 18 - 1, 96):
            substring = s[i:j + 1]
            if len(substring) >= 18 and len(substring) <= 47:
                if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes