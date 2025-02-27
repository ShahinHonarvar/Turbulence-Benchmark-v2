def filter_chars(s):
    chars_to_remove = [s[i] for i in range(44, 59) if '/' < s[i] < '6']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s