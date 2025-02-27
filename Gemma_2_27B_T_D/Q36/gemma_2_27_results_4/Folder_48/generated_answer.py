def filter_chars(s):
    chars_to_remove = set()
    for i in range(154, 222):
        if 'A' < chr(i) < 'f':
            chars_to_remove.add(chr(i))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s