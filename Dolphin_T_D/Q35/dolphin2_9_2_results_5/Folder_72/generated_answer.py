def remove_repeat_chars(s):
    char_count = {}
    for i in range(13, 70):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    repeat_chars = [c for c, v in char_count.items() if v > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s