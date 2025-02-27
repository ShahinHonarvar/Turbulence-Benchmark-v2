def palindromes_of_specific_lengths(s):
    substring = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.lower() == sub[:] and sub.isalpha():
                palindromes.add(sub)
    return palindromes