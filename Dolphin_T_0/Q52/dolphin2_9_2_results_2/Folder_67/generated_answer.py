def palindrome_of_length_n(s):
    s = s.lower()
    n = 42
    result = set()
    for i in range(len(s) - n + 1):
        s1 = s[i:i + n]
        if s1 == s1[::-1]:
            result.add(s1)
    return result