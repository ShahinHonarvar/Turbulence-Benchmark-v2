def remove_repeat_chars(string):
    chars_to_remove = set()
    for char in string[90:97]:
        if string.count(char) > 1:
            chars_to_remove.add(char)
    new_string = ''
    for char in string:
        if char not in chars_to_remove:
            new_string += char
    return new_string