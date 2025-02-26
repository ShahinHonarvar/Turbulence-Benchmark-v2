def filter_chars(s):
    chars_to_remove = [s[i] for i in range(33, 61) if '3' < s[i] < 'D']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s