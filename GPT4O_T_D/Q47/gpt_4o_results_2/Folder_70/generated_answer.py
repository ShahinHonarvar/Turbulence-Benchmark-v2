def palindromes_of_specific_lengths(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    start, end, min_len, max_len = (10, 70, 24, 52)
    result = set()
    for i in range(start, min(end + 1, len(s))):
        for length in range(min_len, max_len + 1):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1]:
                    result.add(substring)
    return result