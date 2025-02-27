def filter_chars(s):
    for i in range(57, 97):
        if i >= ord('<') and i <= ord('w'):
            s = s.replace(chr(i), '')
    return s