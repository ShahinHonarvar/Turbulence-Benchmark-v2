def remove_repeat_chars(string):
    chars_to_remove = set((char for char in string[20:35] if string[20:35].count(char) > 1))
    return ''.join((char for char in string if char not in chars_to_remove))