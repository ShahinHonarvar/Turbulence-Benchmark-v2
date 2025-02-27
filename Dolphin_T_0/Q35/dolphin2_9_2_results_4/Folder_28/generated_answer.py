def remove_repeat_chars(string):
    chars_to_remove = []
    for i in range(86, 99):
        char = string[i]
        if string.count(char) > 1:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string