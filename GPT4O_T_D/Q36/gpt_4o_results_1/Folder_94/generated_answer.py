def filter_chars(s):
    out_str = ''
    for i in range(len(s)):
        if 15 < i < 85 and 'I' < s[i] < 'M':
            continue
        out_str += s[i]
    return out_str