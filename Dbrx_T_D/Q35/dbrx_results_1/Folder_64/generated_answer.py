def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(1, 5):
        if s[i] in s[i + 1:6]:
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s