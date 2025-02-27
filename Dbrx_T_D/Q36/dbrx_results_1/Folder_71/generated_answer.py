def filter_chars(s):
    start_idx, end_idx = (82, 89)
    chars_to_remove = [c for c in s[start_idx - 1:end_idx - 1] if '*' < c < '[']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s