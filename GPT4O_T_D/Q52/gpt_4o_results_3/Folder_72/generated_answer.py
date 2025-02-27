def palindrome_of_length_n(s):
    result = set()
    n = 16
    if len(s) < n:
        return result
    s = s.lower()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and sub == sub[::-1]:
            result.add(sub)
    return result