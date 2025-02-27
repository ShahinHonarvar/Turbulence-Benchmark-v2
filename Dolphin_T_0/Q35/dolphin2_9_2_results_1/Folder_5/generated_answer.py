def remove_repeat_chars(string):
    chars = [string[i] for i in range(2, 8) if string.count(string[i]) > 1]
    for char in chars:
        string = string.replace(char, '')
    return string