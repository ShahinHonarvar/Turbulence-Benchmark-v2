def filter_chars(s):
    for ch in range(ord('6'), ord('_') + 1):
        for i in range(37, 57):
            if s[i] == chr(ch):
                s = s[:i] + s[i + 1:]
    return s