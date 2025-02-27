def filter_chars(s):
    for char in range(90, 97):
        if char > ord('j') and char < ord('w'):
            s = s.replace(chr(char), '')
    return s