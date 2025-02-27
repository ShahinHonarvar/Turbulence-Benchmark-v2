def filter_chars(s):
    for i in range(len(s)):
        if 32 < i < 69:
            char = s[i]
            if 'B' < char < 'v':
                s = s.replace(char, '', 1)
    return s