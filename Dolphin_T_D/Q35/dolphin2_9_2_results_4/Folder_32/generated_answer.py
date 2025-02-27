def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(86, 90):
        char = s[i]
        if s.count(char) > 1:
            chars_to_remove.add(char)
    new_string = ''
    for char in s:
        if char not in chars_to_remove:
            new_string += char
    return new_string