def filter_chars(s):
    chars_to_remove = set()
    for i in range(45, 57):
        char = chr(i)
        if 'F' < char < 'n':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s