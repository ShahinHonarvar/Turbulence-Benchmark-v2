def remove_repeat_chars(s):
    chars_to_remove = {}
    for i in range(36, 85):
        if chars_to_remove.get(s[i], False):
            chars_to_remove[s[i]] += 1
        else:
            chars_to_remove[s[i]] = 1
    for char, count in chars_to_remove.items():
        if count > 1:
            s = s.replace(char, '')
    return s