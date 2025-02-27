def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(34, 69):
        if s[i] in s[i + 1:69]:
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s