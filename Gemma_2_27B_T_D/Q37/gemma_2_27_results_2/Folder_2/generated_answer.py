def filter_chars(s):
    for i in range(477, 985):
        if len(s) > i and ',' <= s[i] <= 'V':
            s = s.replace(s[i], '')
    return s