def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    result = set()
    for i in range(n - 146):
        substring = s[i:i + 147]
        if substring == substring[::-1]:
            result.add(substring)
    return result