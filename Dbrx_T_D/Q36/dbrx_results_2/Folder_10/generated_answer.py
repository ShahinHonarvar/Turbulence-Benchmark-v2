def filter_chars(s):
    for i in range(len(s)):
        if 35 < i < 60:
            char = s[i]
            if '!' < char < 'B':
                s = s.replace(char, '', 1)
    return s