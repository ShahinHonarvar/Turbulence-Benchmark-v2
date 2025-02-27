def palindromes_of_specific_lengths(s):
    s = s[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes