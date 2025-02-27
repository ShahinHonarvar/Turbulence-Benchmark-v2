def palindromes_of_specific_lengths(s):
    s = s[70:141]
    result = set()
    for length in range(3, 61):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs[::-1].lower():
                result.add(subs)
    return result