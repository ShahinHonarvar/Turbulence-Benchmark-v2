def remove_repeat_chars(s):
    char_dict = {}
    for c in s[56:88]:
        char_dict[c] = char_dict.get(c, 0) + 1
    for c in list(s):
        if char_dict.get(c, 0) > 1:
            s = s.replace(c, '')
    return s