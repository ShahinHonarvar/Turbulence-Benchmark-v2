def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 79, -1, -1):
        for j in range(i + 80, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                res.add(s[i:j])
    return res