def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(1, 7):
        if s[i] in s[i + 1:]:
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s