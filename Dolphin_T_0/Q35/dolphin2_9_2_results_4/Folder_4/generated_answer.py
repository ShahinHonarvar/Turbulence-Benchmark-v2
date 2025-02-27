def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(49, 74):
        chars = s[i]
        if s.count(chars) > 1:
            chars_to_remove.add(chars)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s