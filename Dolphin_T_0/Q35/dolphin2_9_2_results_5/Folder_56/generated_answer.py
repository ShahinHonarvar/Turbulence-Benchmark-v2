def remove_repeat_chars(string):
    chars = set()
    for i in range(7, 10):
        if string[i] not in chars:
            chars.add(string[i])
    for char in chars:
        string = string.replace(char, '')
    return string