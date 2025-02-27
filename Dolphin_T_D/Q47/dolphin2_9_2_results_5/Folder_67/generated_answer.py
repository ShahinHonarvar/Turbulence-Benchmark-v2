def palindromes_of_specific_lengths(s):
    s = s[65:100]
    pal = set()
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs.lower() and subs == subs.upper() and (subs == subs[::-1]):
                pal.add(subs)
    return pal