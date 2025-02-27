def filter_chars(s):
    chars_to_remove = []
    for i in range(43, 68):
        if i >= ord('t') and i <= ord('x'):
            chars_to_remove.append(chr(i))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s