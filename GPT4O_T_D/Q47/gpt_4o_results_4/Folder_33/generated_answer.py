def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s[130:296] if c.isalpha())).lower()
    result = set()
    for length in range(103, 159):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result