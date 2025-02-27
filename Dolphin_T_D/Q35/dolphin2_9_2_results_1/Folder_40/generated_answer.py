def remove_repeat_chars(string):
    chars_to_remove = [char for char in string[1:4] if string.count(char) > 1]
    return ''.join((char for char in string if char not in chars_to_remove))