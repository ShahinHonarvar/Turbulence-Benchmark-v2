def filter_chars(s):
    chars_to_remove = [s[i] for i in range(3, 5) if 'Y' < s[i] < 's']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s