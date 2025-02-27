def filter_chars(s):
    chars_to_remove = []
    for i in range(43, 67):
        if i >= ord('7') and i <= ord('f'):
            chars_to_remove.append(chr(i))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s