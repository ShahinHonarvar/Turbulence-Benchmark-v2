def filter_chars(s):
    chars_to_remove = [s[i] for i in range(33, 36) if '>' < s[i] < 'A']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s