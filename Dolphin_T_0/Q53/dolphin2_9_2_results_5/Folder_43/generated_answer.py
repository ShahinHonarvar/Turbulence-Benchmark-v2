def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    p = set()
    for i in range(len(s) - 48):
        for j in range(i + 49, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                p.add(s[i:j])
    return p