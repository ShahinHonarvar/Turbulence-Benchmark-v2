def filter_chars(s):
    chars_to_remove = [s[i] for i in range(29, 33) if s[i] > '%' and s[i] < 'a']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s