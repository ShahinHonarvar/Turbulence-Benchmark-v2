def filter_chars(s):
    chars_to_remove = [s[i] for i in range(48, 75) if '6' < s[i] < '_']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s