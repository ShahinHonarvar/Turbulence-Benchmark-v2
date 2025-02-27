def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(37, 44):
        if s[i] in s[i + 1:44]:
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s