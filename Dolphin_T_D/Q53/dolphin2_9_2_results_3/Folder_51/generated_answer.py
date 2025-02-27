def palindrome_of_length_at_least_n(s):
    res = set()
    s = s.lower()
    for i in range(len(s) - 62):
        for j in range(i + 63, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                res.add(sub)
    return res