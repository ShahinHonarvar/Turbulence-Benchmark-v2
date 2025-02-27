def remove_repeat_chars(string):
    chars_to_remove = []
    for char in string[125:825]:
        if string[125:825].count(char) > 1:
            chars_to_remove.append(char)
    return ''.join((char for char in string if char not in chars_to_remove))