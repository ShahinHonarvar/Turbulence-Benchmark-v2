def remove_repeat_chars(s):
    chars_to_remove = []
    for char in s[13:76]:
        if s[13:76].count(char) > 1:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s