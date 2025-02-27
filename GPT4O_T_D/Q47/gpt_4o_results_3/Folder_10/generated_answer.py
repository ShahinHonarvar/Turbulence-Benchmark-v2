def palindromes_of_specific_lengths(s):
    s = s[16:61]
    result = set()
    lower_s = ''.join(filter(str.isalpha, s.lower()))
    n = len(lower_s)
    for start in range(n):
        for end in range(start + 15, min(start + 39, n)):
            substr = lower_s[start:end + 1]
            if substr == substr[::-1]:
                result.add(lower_s[start:end + 1])
    return result