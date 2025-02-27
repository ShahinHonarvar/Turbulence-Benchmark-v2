def filter_chars(s):
    chars_to_remove = [s[i] for i in range(1, 6) if ',' < s[i] < 'f']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s