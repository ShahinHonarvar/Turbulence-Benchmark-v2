def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 89
    result = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result