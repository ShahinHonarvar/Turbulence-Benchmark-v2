def filter_chars(s):
    chars_to_remove = [s[i] for i in range(45, 57) if 'F' < s[i] < 'n']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s