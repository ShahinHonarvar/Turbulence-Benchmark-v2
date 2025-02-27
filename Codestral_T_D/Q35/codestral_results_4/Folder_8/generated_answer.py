def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(45, 48):
        if string.count(string[i], 45, 48) > 1:
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))