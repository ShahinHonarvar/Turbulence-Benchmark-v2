def filter_chars(s):
    for i in range(63, 85):
        if 'E' <= s[i] <= '~' and s[i].isascii():
            s = s.replace(s[i], '')
    return s