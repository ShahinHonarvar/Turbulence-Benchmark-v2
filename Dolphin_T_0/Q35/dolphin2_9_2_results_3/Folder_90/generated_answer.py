def remove_repeat_chars(string):
    repeat_chars = [string[i] for i in range(306, 807) if string.count(string[i]) > 1]
    for char in repeat_chars:
        string = string.replace(char, '')
    return string