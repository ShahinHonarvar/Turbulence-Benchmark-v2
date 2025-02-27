def palindromes_of_specific_lengths(s):
    s = s[13:96]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    result = set()
    for length in range(57, 61):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1]:
                result.add(subs)
    return result