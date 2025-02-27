def remove_repeat_chars(string):
    repeated_chars = [string[i] for i in range(39, 44) if string.count(string[i]) > 1]
    for char in repeated_chars:
        string = string.replace(char, '')
    return string