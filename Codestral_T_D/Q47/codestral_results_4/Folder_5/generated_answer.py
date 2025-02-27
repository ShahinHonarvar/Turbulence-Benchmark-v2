def palindromes_of_specific_lengths(s):
    s = s[63:71]
    palindromes = set()
    for l in range(4, 6):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes