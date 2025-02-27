def remove_repeat_chars(string):
    chars_to_remove = []
    for i in range(2, 5):
        if string[i] in string[0:2] + string[5:]:
            chars_to_remove.append(string[i])
    return ''.join([char for char in string if char not in chars_to_remove])