def remove_repeat_chars(s):
    char_count = {}
    for i in range(100, 200):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s