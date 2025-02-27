def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        if i + 51 <= len(s) and s[i:i + 51] == s[i:i + 51][::-1]:
            res.add(s[i:i + 51])
    return res