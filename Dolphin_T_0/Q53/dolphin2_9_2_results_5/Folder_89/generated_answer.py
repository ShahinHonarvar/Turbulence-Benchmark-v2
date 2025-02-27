def palindrome_of_length_at_least_n(s):
    s = s.lower()
    a = set()
    for i in range(len(s)):
        for j in range(i + 42, len(s)):
            t = s[i:j + 1]
            if t == t[::-1]:
                a.add(t)
    return a