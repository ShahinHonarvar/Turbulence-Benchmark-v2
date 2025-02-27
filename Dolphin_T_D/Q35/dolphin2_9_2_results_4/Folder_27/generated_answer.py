def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(86, 90):
        char_count = s[i:].count(s[i])
        if char_count > 1:
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s