def palindromes_of_specific_lengths(s):
    s = s[29:99]
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == ''.join(reversed(sub) and sub.isalpha()):
                palindromes.add(''.join(reversed(sub)).lower())
    return palindromes