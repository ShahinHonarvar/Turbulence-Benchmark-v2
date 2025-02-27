def filter_chars(s):
    for c in [chr(i) for i in range(ord('?'), ord('n') + 1)]:
        s = s[:513] + s[513:878].replace(c, '') + s[878:]
    return s