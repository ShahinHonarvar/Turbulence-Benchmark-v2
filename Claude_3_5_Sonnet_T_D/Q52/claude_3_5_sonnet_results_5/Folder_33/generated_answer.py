def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 475
    result = set()
    if len(s) < n:
        return result
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result