def remove_repeat_chars(s):
    char_count = {}
    for i in range(409, 502):
        if s[i] not in char_count:
            char_count[s[i]] = 1
        else:
            char_count[s[i]] += 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s