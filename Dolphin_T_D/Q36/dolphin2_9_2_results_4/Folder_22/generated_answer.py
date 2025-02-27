def filter_chars(s):
    for i in range(len(s)):
        if 55 <= i < 84:
            if ';' < s[i] < 'z':
                s = s.replace(s[i], '')
    return s