def filter_chars(s):
    for i in range(31, 39):
        if i >= ord(';') and i <= ord('g') and (chr(i) in s):
            s = s.replace(chr(i), '')
    return s