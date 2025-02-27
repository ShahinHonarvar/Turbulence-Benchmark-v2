def filter_chars(s):
    chars_to_filter = [chr(i) for i in range(32, 84)]
    for char in chars_to_filter:
        if char > 'm' and char < 'w':
            s = s.replace(char, '')
    return s