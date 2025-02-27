def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(33, 78):
        char = s[i]
        if s.count(char) > 1:
            chars_to_remove.add(char)
    new_s = ''
    for char in s:
        if char not in chars_to_remove:
            new_s += char
    return new_s