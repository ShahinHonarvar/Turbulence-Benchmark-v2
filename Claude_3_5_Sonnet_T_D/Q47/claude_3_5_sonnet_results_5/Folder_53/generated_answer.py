def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s[1:300] if c.isalpha()))
    for i in range(len(s)):
        for j in range(i + 3, min(i + 11, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result