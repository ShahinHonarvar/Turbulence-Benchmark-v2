def filter_chars(s):
    for char in [chr(i) for i in range(ord('!'), ord('T') + 1)]:
        s = s[:20] + s[20:80].replace(char, '') + s[80:]
    return s