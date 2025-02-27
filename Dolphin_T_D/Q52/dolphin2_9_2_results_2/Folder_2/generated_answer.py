def palindrome_of_length_n(s):
    s = s.lower()
    a = set()
    for i in range(len(s)):
        for j in range(i + 146, len(s)):
            t = s[i:j + 1]
            if len(t) == 147 and t == t[::-1] and t.isalpha():
                a.add(t)
    return a