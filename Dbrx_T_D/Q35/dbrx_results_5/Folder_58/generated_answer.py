def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(103, 802):
        if string[i] in chars_to_remove:
            string = string[:i] + string[i + 1:]
        else:
            chars_to_remove.add(string[i])
    return string