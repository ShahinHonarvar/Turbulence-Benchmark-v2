def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[27:96]
    for length in range(49, 52):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes