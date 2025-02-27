def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    p = set()
    for i in range(len(s)):
        for j in range(i + 87, len(s) + 1):
            sub = s[i:j]
            if len(sub) >= 87 and sub == sub[::-1]:
                p.add(sub)
    return p