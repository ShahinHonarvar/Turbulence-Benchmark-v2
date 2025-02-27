def palindrome_of_length_n(s):
    res = set()
    s = s.lower()
    for i in range(len(s) - 42):
        temp = s[i:i + 43]
        if temp == temp[::-1]:
            res.add(temp)
    return res