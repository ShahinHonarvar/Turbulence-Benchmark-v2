def palindromes_of_specific_lengths(s):
    result = set()
    s = s[65:100]
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs.lower() and subs[::-1] == subs.lower()[::-1]:
                result.add(subs)
    return result