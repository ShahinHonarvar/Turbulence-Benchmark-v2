def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 92):
        sub = s[i:i + 93]
        if sub == sub[::-1] and sub.isalpha():
            res.add(sub)
    return res