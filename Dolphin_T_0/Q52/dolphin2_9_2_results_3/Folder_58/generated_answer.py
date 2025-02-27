def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 223 + 1):
        substring = s[i:i + 223]
        if substring == substring[::-1]:
            res.add(substring)
    return res