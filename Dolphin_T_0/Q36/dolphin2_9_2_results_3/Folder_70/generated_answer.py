def filter_chars(s):
    for char in range(ord('!'), ord('{')):
        if char in s:
            s = s.replace(chr(char), '')
    return s