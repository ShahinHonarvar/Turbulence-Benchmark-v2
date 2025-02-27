def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(25, 80):
        if string.count(string[i]) > 1:
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))