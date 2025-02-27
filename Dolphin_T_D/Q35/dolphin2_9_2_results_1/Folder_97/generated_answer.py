def remove_repeat_chars(string):
    chars = [char for char in string if string.count(char) == 1]
    return ''.join(chars)