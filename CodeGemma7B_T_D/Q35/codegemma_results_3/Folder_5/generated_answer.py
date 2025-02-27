def remove_repeat_chars(string):
    for i in range(2, 8):
        if string[i] in string[i + 1:]:
            while string[i] in string[i + 1:]:
                string = string[:i] + string[i + 1:]
    return string