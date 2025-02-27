def filter_chars(s):
    for i in range(36, 80):
        if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('i'):
            s = s[:i] + s[i + 1:]
    return s