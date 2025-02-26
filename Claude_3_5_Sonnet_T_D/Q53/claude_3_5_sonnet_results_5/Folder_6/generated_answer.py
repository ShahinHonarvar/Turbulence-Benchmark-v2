def palindrome_of_length_at_least_n(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    for i in range(n):
        for j in range(i + 22, n + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result