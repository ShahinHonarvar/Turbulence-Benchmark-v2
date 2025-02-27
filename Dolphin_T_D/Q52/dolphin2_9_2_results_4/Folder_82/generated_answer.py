def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 27):
        if s[i:i + 28] == s[i:i + 28][::-1] and s[i:i + 28].isalpha():
            res.add(s[i:i + 28])
    return res