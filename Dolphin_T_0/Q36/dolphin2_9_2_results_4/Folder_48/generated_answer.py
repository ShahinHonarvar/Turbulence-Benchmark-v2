def filter_chars(s):
    chars_to_remove = [s[i] for i in range(154, 222) if 'A' < s[i] < 'f']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s