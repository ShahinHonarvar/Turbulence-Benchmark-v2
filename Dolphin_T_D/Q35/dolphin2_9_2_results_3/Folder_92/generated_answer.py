def remove_repeat_chars(string):
    chars_to_remove = [string[i] for i in range(1, len(string) - 1) if string.count(string[i]) > 1]
    return ''.join([char for char in string if char not in chars_to_remove])