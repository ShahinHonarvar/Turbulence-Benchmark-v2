def palindrome_of_length_at_least_n(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    for i in range(n):
        for j in range(i + 88, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result