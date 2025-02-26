def filter_chars(s):
    chars_to_remove = []
    for i in range(91, 97):
        if i > ord('j') and i < ord('w'):
            chars_to_remove.append(chr(i))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s