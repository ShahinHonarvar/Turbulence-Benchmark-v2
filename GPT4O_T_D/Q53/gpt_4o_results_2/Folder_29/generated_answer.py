def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for start in range(n):
        for end in range(start + 78, n + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                result.add(substring)
    return result