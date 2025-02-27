def filter_chars(s):
    for i in range(477, 985):
        if ord(s[i]) >= ord(',') and ord(s[i]) <= ord('V'):
            s = s[:i] + s[i + 1:]
    return s