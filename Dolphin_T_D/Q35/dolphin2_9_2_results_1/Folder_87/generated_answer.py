def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in s[20:43]:
        if s.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.add(char)
    new_string = ''
    for char in s:
        if char not in chars_to_remove:
            new_string += char
    return new_string