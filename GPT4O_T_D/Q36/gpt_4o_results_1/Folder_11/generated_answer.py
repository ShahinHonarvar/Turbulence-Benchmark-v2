def filter_chars(s):
    if len(s) <= 86:
        return s
    filtered_s = s
    for i in range(87, min(93, len(s))):
        if 'E' < s[i] < '~':
            filtered_s = filtered_s.replace(s[i], '')
    return filtered_s