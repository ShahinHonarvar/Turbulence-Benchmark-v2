def remove_repeat_chars(s):
    char_count = {}
    for i in range(50, 92):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for key, value in char_count.items():
        if value > 1:
            s = s.replace(key, '')
    return s