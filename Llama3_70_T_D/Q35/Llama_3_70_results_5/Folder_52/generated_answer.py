def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(39, 80):
        if s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    new_s = ''
    for char in s:
        if char not in chars_to_remove:
            new_s += char
    return new_s