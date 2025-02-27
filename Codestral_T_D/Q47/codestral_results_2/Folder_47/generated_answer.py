def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes