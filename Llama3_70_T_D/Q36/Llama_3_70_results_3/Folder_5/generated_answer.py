def filter_chars(s):
    chars_to_remove = [s[i] for i in range(55, 66) if 'f' < s[i] < '|']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s