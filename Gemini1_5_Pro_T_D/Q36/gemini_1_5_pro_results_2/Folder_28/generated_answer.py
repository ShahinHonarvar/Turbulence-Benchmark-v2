def filter_chars(s):
    chars_to_remove = []
    for i in range(32, 73):
        if chr(i) > 'M' and chr(i) < 'j':
            chars_to_remove.append(chr(i))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s