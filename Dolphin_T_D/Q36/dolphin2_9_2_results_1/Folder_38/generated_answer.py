def filter_chars(s):
    chars_to_remove = [s[i] for i in range(44, 48) if s[i] > '+' and s[i] < 'l']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s