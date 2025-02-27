def remove_repeat_chars(s):
    char_count = {}
    for i in range(80, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = [k for k, v in char_count.items() if v > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s