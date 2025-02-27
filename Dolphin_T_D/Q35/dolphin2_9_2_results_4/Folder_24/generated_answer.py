def remove_repeat_chars(s):
    char_count = {}
    for c in s[13:91]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in char_count:
        if char_count[c] > 1:
            s = s.replace(c, '')
    return s