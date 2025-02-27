def remove_repeat_chars(string):
    for i in range(13, 91):
        c = string[i]
        string = string.replace(c, '')
    return string