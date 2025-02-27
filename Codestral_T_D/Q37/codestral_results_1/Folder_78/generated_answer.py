def filter_chars(s):
    for char in range(ord('8'), ord('e') + 1):
        char = chr(char)
        if 75 <= s.find(char) <= 99:
            s = s.replace(char, '')
    return s