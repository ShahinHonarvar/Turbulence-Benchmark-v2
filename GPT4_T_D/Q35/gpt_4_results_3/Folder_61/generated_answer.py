def remove_repeat_chars(string):
    repeat_chars = [char for char in string[1:8] if string[1:8].count(char) > 1]
    return ''.join((char for char in string if char not in repeat_chars))