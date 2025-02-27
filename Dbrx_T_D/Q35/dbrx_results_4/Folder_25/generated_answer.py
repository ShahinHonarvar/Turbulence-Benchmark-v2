def remove_repeat_chars(s):
    for i in range(37, 43):
        char = s[i]
        s = s[:i] + s[i + 1:].replace(char, '')
    return s