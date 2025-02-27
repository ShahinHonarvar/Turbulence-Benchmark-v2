def palindromes_of_specific_lengths(s):
    result = set()
    s = s[24:98]
    s = ''.join(filter(str.isalpha, s))
    s_lower = s.lower()
    for length in range(10, 37):
        for start in range(len(s) - length + 1):
            substr = s_lower[start:start + length]
            if substr == substr[::-1]:
                result.add(s[start:start + length])
    return result