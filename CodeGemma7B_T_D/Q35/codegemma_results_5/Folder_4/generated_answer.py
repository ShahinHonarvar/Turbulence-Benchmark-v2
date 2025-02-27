def remove_repeat_chars(string):
    for i in range(49, 74):
        if string[i] in string[i + 1:]:
            string = string.replace(string[i], '')
    return string