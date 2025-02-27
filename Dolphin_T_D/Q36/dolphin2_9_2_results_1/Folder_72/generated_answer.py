def filter_chars(s):
    chars_to_filter = {}
    for i in range(44, 68):
        if 'W' < s[i] < 'x':
            chars_to_filter[s[i]] = True
    s = ''.join((c for c in s if c not in chars_to_filter))
    return s