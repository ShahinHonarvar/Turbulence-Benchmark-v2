def palindromes_of_specific_lengths(s):
    sub = s[1:9]
    sub = ''.join((c for c in sub if c.isalpha()))
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(sub) - length + 1):
            si = sub[i:i + length]
            if si.lower() == si.lower()[::-1]:
                palindromes.add(si)
    return palindromes