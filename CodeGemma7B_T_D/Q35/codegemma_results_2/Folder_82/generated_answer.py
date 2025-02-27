def remove_repeat_chars(string):
    for i in range(len(string)):
        if string[i] in string[30:200] and string.count(string[i]) > 1:
            string = string.replace(string[i], '')
    return string