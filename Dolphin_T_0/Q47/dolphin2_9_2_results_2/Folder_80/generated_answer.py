def palindromes_of_specific_lengths(s):
    s = s[35:89]
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs.lower() and subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes