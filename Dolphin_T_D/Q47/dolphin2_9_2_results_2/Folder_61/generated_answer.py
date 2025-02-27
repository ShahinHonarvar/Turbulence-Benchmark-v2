def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:31]
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            if len(set(s[i:i + length])) > 1:
                continue
            subs = s[i:i + length]
            if subs == subs[::-1]:
                result.add(subs.lower())
    return result