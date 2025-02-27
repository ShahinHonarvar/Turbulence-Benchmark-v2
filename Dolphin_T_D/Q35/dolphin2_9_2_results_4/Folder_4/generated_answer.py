def remove_repeat_chars(s):
    count = [0] * 128
    for i in range(49, 75):
        if count[ord(s[i])] == 1:
            s = s[:i] + s[i + 1:]
            count = [0] * 128
    return s