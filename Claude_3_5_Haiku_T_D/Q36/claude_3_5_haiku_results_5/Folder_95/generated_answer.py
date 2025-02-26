def filter_chars(s):
    chars_to_remove = [s[i] for i in range(57, 86) if s[i] > '+' and s[i] < 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s