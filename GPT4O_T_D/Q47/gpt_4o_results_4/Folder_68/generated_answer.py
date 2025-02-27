def palindromes_of_specific_lengths(s):
    s = s[:51]
    s = ''.join([c.lower() for c in s if c.isalpha()])
    result = set()
    n = len(s)
    for length in range(50, 101):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result