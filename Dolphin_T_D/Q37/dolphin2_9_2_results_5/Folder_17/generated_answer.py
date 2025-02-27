def filter_chars(s):
    char_range = [';', 'b']
    for i in range(27, 30):
        if char_range[0] <= s[i] <= char_range[1]:
            s = s.replace(s[i], '')
    return s