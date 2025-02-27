def remove_repeat_chars(string):
    to_remove = [char for char, count in zip(string[20:43], string.count(char)[20:43]) if count > 1]
    return ''.join([char for char in string if char not in to_remove])