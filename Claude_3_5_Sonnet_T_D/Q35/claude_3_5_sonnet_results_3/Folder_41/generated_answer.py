def remove_repeat_chars(string):
    repeated_chars = set([char for char in string[4:8] if string[4:8].count(char) > 1])
    return ''.join([char for char in string if char not in repeated_chars])