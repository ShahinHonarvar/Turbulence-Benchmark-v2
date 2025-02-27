def palindromes_of_specific_lengths(s):
    s = s[30:85]
    s = ''.join((c for c in s if c.isalpha()))
    result = set()
    for length in range(12, 21):
        for idx in range(len(s) - length + 1):
            subs = s[idx:idx + length]
            if subs == subs[::-1]:
                result.add(subs.lower())
    return result