def filter_chars(s):
    filtered_chars = [c for c in s if c > 'f' and c < '~' and (344 <= s.index(c) < 874)]
    for fc in filtered_chars:
        s = s.replace(fc, '')
    return s