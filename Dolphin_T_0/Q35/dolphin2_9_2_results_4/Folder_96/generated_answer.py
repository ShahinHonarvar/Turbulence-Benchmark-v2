def remove_repeat_chars(s):
    char_to_count = {}
    for i in range(60, 200):
        c = s[i]
        char_to_count[c] = char_to_count.get(c, 0) + 1
    for c in char_to_count:
        if char_to_count[c] > 1:
            s = s.replace(c, '')
    return s