def palindrome_of_length_at_least_n(s):
    s = s.lower()
    l = len(s)
    p = set()
    for i in range(l):
        for j in range(i + 36, l):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                p.add(s[i:j + 1])
    return p