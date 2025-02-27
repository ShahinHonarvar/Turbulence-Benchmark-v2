def palindromes_of_specific_lengths(s):
    s = s[32:80]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    result = set()
    for length in range(35, 42):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result