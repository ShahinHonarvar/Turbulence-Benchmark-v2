def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(43, 48):
        for i in range(16, 78):
            if len(s) - i + 1 < length:
                break
            subs = s[i:i + length]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result