def palindrome_of_length_at_least_n(s):
    result = set()
    s = ''.join((char.lower() for char in s if char.isalpha()))
    n = len(s)
    for i in range(n):
        for j in range(i + 23, n + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result