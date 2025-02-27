def palindrome_of_length_n(s):
    s = s.lower()
    a = set()
    for i in range(len(s) - 422):
        if s[i:i + 423] == s[i:i + 423][::-1]:
            a.add(s[i:i + 423])
    return a