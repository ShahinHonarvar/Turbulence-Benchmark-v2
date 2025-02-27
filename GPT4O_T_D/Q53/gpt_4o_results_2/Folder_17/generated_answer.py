def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 36, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result