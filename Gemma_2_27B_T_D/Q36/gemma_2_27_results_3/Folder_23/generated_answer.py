def filter_chars(s):
    chars_to_remove = set()
    for i in range(21, 25):
        if '5' < s[i] < '}':
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s