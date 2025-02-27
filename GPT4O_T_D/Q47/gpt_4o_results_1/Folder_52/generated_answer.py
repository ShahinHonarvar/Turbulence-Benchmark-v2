def palindromes_of_specific_lengths(s):
    s = s[44:100]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    n = len(s)
    for length in range(13, 43):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result