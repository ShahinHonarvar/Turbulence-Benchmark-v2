def palindrome_of_length_at_least_n(s):
    res = set()
    s1 = s.lower()
    for i in range(len(s) - 1):
        for j in range(i + 2, len(s) + 1):
            if s1[i:j] == s1[i:j][::-1]:
                if len(s1[i:j]) >= 144:
                    res.add(s[i:j])
    return res