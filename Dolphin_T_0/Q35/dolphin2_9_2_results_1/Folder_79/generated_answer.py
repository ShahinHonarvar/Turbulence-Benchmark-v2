def remove_repeat_chars(string):
    chars_to_remove = [char for char in string[1:7] if string.count(char) > 1]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string