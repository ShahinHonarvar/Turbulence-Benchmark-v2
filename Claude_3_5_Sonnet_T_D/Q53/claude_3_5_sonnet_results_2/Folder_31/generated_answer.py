def palindrome_of_length_at_least_n(s):
    result = set()
    s = ''.join((char.lower() for char in s if char.isalpha()))
    n = len(s)
    for i in range(n):
        for j in range(i + 34, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result