def remove_repeat_chars(s):
    for i in range(1, 5):
        char = s[i]
        count = s[1:i].count(char)
        if count > 0:
            s = s[:i] + s[i:].replace(char, '')
    return s