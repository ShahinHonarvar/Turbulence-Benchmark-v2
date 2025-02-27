def palindromes_of_specific_lengths(s):
    s = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes