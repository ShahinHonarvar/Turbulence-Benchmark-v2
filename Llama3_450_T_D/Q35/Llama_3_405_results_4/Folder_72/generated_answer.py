def remove_repeat_chars(s):
    char_count = {}
    for i in range(13, 70):
        try:
            char_count[s[i]] += 1
        except KeyError:
            char_count[s[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s