def remove_repeat_chars(s):
    chars = {}
    for i in range(77, 84):
        if s[i] not in chars:
            chars[s[i]] = 1
        else:
            chars[s[i]] += 1
    for char, count in chars.items():
        if count > 1:
            s = s.replace(char, '')
    return s