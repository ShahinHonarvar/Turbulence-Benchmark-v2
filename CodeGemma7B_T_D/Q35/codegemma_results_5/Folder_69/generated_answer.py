def remove_repeat_chars(string):
    for i in range(39, 43):
        if string[i] in string[43:]:
            string = string.replace(string[i], '', string.count(string[i]))
    return string