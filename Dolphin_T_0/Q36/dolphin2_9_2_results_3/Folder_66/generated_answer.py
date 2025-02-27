def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(40, 87) if chr(i) > '!' and chr(i) < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s