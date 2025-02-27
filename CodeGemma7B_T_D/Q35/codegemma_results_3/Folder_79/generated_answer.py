def remove_repeat_chars(string):
    if string[1:7] == string[1:7]:
        for i in range(1, 7):
            string = string.replace(string[i], '')
    return string