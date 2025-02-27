def remove_repeat_chars(string):
    repeat_chars = [char for char in string[36:86] if string.count(char) > 1]
    return ''.join([char for char in string if char not in repeat_chars])