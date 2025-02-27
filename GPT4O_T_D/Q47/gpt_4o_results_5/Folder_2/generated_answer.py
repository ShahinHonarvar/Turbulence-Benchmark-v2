def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s[10:60] if c.isalpha())).lower()
    result = set()
    n = len(s)
    for length in range(18, 37):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result