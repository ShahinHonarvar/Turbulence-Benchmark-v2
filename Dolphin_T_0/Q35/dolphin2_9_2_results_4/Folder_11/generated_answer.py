def remove_repeat_chars(s):
    char_dict = {}
    for i in range(48, 76):
        if s[i] in char_dict:
            char_dict[s[i]] = 2
        elif s[i] not in char_dict:
            char_dict[s[i]] = 1
    for char, value in char_dict.items():
        if value > 1:
            s = s.replace(char, '')
    return s