def remove_repeat_chars(string):
    for i in range(22, 24):
        if string[i] in string[i + 1:]:
            while string[i] in string:
                string = string.replace(string[i], '')
    return string