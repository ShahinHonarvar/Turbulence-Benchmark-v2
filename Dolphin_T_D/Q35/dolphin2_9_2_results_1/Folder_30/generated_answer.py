def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(22, 25):
        if string[i] in string[i + 1:]:
            chars_to_remove.add(string[i])
    return ''.join([char for char in string if char not in chars_to_remove])