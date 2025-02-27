def filter_chars(s):
    for c in [chr(i) for i in range(ord('*'), ord('b') + 1)]:
        s = s[:42] + s[42:98].replace(c, '') + s[98:]
    return s