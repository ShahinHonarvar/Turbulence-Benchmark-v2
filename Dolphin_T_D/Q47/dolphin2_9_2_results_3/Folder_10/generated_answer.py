def palindromes_of_specific_lengths(s):
    s = s[15:60]
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if all([c.isalpha() for c in sub]) and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes