def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 23
    result = set()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result