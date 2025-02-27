def filter_chars(s):
    for i in range(len(s)):
        if 38 < i < 81 and '.' < s[i] < '^':
            s = s.replace(s[i], '', 1)
            i -= 1
    return s