def palindromes_of_specific_lengths(s):
    result = set()
    s = s[11:123]
    for length in range(12, 221):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs.lower())
    return result