def filter_chars(s):
    for char in range(ord('O'), ord('^') + 1):
        s = s.replace(chr(char), '')
    for i in range(17, 64):
        s = s[:i] + s[i].replace('', '') + s[i + 1:]
    return s