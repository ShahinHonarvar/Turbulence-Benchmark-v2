def remove_repeat_chars(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1] and i + 1 > 37 and (i + 1 < 43):
            s = s[:i] + s[i + 1:]
            i -= 1
    return s