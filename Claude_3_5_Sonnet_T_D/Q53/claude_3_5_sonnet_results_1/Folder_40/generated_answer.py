def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 3:
                result.add(substring)
    return result