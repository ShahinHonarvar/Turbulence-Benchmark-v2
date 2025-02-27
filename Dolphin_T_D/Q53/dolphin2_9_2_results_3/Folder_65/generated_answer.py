def palindrome_of_length_at_least_n(s):
    g = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 15, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                g.add(s[i:j].upper())
    return g