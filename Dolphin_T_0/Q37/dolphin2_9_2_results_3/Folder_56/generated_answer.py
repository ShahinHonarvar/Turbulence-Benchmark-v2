def filter_chars(s):
    for char in range(ord('K'), ord('a') + 1):
        for i in range(71, 95):
            if char == ord(s[i]):
                s = s[:i] + s[i + 1:]
    return s