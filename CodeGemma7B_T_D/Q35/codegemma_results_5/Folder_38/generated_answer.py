def remove_repeat_chars(s):
    for i in range(len(s)):
        if s[i] in s[36:85] and s.count(s[i]) > 1:
            s = s.replace(s[i], '', s.count(s[i]) - 1)
    return s