def filter_chars(s):
    for char in s:
        if ord(char) >= ord('5') and ord(char) <= ord('_'):
            s = s.replace(char, '')
    return s