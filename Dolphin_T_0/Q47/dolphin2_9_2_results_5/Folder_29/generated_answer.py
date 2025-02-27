def palindromes_of_specific_lengths(s):
    s = s[14:94]
    result = set()
    for length in range(18, 74):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result