def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('%') + 1, ord('a'))]
    for char in chars_to_remove:
        if 29 < s.find(char) < 33:
            s = s.replace(char, '')
    return s