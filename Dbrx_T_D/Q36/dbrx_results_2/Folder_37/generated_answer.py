def filter_chars(s):
    for i in range(len(s)):
        if 44 < i < 59:
            char = s[i]
            if '/' < char < '6':
                s = s.replace(char, '', 1)
    return s