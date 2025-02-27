def filter_chars(s):
    for char in range(ord('f'), ord('o') + 1):
        s = s[:19] + s[19:33].replace(chr(char), '') + s[33:]
    return s