def remove_repeat_chars(string):
    chars_to_remove = set()
    for char in string[57:84]:
        if string.count(char) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))