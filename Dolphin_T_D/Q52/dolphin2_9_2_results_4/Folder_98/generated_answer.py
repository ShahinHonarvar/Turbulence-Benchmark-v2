def palindrome_of_length_n(s):
    res = set()
    s = s.lower()
    for i in range(len(s) - 5):
        for j in range(i + 3, len(s)):
            if s[i] == s[j] and (s[i + 1] == s[j - 1] if j - i > 2 else True):
                res.add(s[i:j + 1])
    return res