def remove_repeat_chars(string):
    slice = string[331:543]
    chars_to_remove = {char for char in slice if slice.count(char) > 1}
    return ''.join((char for char in string if char not in chars_to_remove))