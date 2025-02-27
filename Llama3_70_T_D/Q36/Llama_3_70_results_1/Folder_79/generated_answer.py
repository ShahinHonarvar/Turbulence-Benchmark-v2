def filter_chars(s):
    chars_to_remove = [s[i] for i in range(11, 46) if '!' < s[i] < 'A']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s