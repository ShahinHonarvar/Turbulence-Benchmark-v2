def remove_repeat_chars(s):
    for i in range(36, 52):
        char = s[i]
        while char in s[i + 1:]:
            s = s[:i] + s[i + 1:]
    return s