def palindrome_of_length_n(s):
    ret = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) == 54:
                ret.add(sub)
    return ret