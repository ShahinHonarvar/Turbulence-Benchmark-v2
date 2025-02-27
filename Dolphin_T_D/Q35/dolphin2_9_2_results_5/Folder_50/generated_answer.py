def remove_repeat_chars(string):
    repeated_chars = [char for char in string[13:76] if string[13:76].count(char) > 1]
    return ''.join([char for char in string if char not in repeated_chars])