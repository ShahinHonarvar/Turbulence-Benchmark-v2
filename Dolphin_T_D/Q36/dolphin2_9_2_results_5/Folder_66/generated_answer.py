def filter_chars(s):
    for i in range(39, 87):
        if ord(s[i]) > ord('!') and ord(s[i]) < ord('}'):
            s = s[:i] + s[i + 1:]
    return s