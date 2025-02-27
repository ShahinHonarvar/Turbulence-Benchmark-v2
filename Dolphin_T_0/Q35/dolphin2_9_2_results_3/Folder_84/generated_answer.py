def remove_repeat_chars(string):
    chars_to_remove = [char for char in string if string.count(char) > 1 and 32 <= string.index(char) < 44]
    return ''.join([char for char in string if char not in chars_to_remove])