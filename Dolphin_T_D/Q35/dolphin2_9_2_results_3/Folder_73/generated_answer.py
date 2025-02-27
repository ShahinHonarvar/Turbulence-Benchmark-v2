def remove_repeat_chars(string):
    chars = [char for char in string[10:76] if string.count(char) > 1]
    for char in chars:
        string = string.replace(char, '')
    return string