def palindromes_of_specific_lengths(s):
    s = s[20:75]
    result = set()
    for length in range(36, 43):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            subs = ''.join((c for c in subs if c.isalpha()))
            subs = subs.lower()
            if subs == subs[::-1] and len(subs) in range(36, 43):
                result.add(subs)
    return result