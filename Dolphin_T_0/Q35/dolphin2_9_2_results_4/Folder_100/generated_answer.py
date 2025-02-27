def remove_repeat_chars(s):
    char_count = {}
    for c in s[44:78]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c, count in char_count.items():
        if count > 1:
            s = s.replace(c, '')
    return s