def remove_repeat_chars(string):
    chars = [string[i] for i in range(19, 33) if string[i] in string[:19] or string[i] in string[33:]]
    for char in chars:
        string = string.replace(char, '')
    return string