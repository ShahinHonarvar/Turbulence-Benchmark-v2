def remove_repeat_chars(string):
    for i in range(2, 8):
        if string[i] in string[:i] + string[i + 1:]:
            while string[i] in string:
                string = string.replace(string[i], '')
    return string