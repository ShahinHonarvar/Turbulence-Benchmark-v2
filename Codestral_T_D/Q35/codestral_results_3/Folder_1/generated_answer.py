def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(17, 88):
        if string[i] in string[i + 1:88] and string[i] not in chars_to_remove:
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))