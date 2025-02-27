def palindromes_of_specific_lengths(s):
    s = s[:31]
    result = set()
    for length in range(20, 31):
        for i in range(0, len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs.lower()[::-1]:
                result.add(subs)
    return result