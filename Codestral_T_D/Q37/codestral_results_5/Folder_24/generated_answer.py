def filter_chars(s):
    for char in map(chr, range(ord('2'), ord('s') + 1)):
        s = s[:36] + s[36:79].replace(char, '') + s[79:]
    return s