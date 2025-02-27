def filter_chars(s):
    chars_to_remove = [s[i] for i in range(29, 33) if '%' < s[i] < 'a']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s