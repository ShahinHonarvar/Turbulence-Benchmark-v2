def filter_chars(s):
    chars_to_filter = []
    for i in range(13, 40):
        ch = s[i]
        if ':' < ch < 'C':
            chars_to_filter.append(ch)
    return ''.join((c for c in s if c not in chars_to_filter))