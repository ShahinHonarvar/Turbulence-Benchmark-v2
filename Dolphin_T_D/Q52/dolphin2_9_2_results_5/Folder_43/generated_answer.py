def palindrome_of_length_n(s):
    s = s.lower()
    n = 51
    p = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            p.add(s[i:i + n])
    return p