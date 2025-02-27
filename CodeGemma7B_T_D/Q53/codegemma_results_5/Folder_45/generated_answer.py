def palindrome_of_length_at_least_n(s):
    s = s.lower()
    ret = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j] and j - i + 1 >= 47:
                pal = s[i:j + 1]
                if pal not in ret:
                    ret.add(pal)
    return ret