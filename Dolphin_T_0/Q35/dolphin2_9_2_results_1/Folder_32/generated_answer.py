def remove_repeat_chars(my_string):
    chars_to_remove = [char for char in my_string[86:91] if my_string.count(char, 86, 91) > 1]
    for char in chars_to_remove:
        my_string = my_string.replace(char, '')
    return my_string