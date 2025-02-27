def filter_chars(s):
    for char in [chr(c) for c in range(ord('A'), ord('b') + 1)]:
        s = s[:35] + s[35:99].replace(char, '') + s[99:]
    return s