def remove_repeat_chars(string):
    chars_to_remove = [char for char in set(string[100:200]) if string.count(char) > 1]
    new_string = ''.join((char for char in string if char not in chars_to_remove))
    return new_string