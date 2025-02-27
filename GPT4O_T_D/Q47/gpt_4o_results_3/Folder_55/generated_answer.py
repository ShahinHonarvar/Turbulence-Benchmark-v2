def palindromes_of_specific_lengths(s):
    result = set()
    filtered = ''.join((c.lower() for c in s[10:76] if c.isalpha()))
    n = len(filtered)
    for length in range(10, 21):
        for i in range(n - length + 1):
            substring = filtered[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result