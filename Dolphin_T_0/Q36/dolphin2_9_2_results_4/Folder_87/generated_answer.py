def filter_chars(s):
    for char in range(32, 61):
        if char > ord('3') and char < ord('D'):
            s = s.replace(chr(char), '')
    return s