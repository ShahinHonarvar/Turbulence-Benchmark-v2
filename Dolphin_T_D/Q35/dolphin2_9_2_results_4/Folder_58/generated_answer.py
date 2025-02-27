def remove_repeat_chars(s):
    char_count = {}
    for c in s[103:802]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for key, value in char_count.items():
        if value > 1:
            s = s.replace(key, '')
    return s