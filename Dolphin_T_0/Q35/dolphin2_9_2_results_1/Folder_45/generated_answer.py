def remove_repeat_chars(s):
    char_count = {}
    for i in range(40, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s