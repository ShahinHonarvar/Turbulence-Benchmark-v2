def filter_chars(s):
    for char in range(476, 948):
        if char > 'b' and char < 'd':
            s = s.replace(chr(char), '')
    return s