def palindrome_of_length_n(s):
    s = s.lower()
    n = 445
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            result.add(sub)
    return result