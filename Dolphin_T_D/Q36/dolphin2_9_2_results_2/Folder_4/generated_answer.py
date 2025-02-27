def filter_chars(s):
    chars_to_remove = [s[i] for i in range(42, 67) if '6' < s[i] < 'g']
    for r in chars_to_remove:
        s = s.replace(r, '')
    return s