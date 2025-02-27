def remove_repeat_chars(s):
    char_count = {}
    for c in s[11:76]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in list(char_count.keys()):
        if char_count[c] > 1:
            s = s.replace(c, '')
    return s