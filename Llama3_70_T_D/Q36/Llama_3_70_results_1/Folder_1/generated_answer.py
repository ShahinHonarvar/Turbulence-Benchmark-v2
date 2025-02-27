def filter_chars(s):
    chars_to_remove = [s[i] for i in range(69, 87) if '#' < s[i] < 'L']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s