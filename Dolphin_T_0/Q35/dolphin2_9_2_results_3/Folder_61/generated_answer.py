def remove_repeat_chars(string):
    if len(string) <= 8:
        return string
    chars_to_remove = []
    for i in range(1, len(string) - 1):
        if string.count(string[i]) > 1:
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string