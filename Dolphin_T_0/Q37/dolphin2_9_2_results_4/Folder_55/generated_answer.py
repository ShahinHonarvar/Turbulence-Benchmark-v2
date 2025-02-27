def filter_chars(s):
    chars_to_remove = [s[i] for i in range(1, 6) if s[i] >= '$' and s[i] <= ';']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s