def filter_chars(s):
    chars_to_remove = [s[i] for i in range(41, 56) if 'Z' < s[i] < 'c']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s