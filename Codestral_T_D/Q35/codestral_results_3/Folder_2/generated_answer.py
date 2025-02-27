def remove_repeat_chars(string):
    substring = string[72:93]
    chars_to_remove = [char for char in substring if substring.count(char) > 1]
    return ''.join((char for char in string if char not in chars_to_remove))