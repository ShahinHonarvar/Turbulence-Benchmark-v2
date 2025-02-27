def palindromes_of_specific_lengths(s):
    s = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for i in range(0, len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes