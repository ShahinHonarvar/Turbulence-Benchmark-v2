def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 30, n):
            substr = s[i:j + 1]
            if substr == substr[::-1]:
                result.add(substr)
    return result