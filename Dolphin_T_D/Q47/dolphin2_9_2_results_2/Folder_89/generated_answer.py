def palindromes_of_specific_lengths(s):
    substring = s[18:89]
    substring = ''.join((c for c in substring if c.isalpha()))
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(substring)):
            subs = substring[i:i + length].lower()
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes