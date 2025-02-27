def remove_repeat_chars(string):
    temp = string[37:43]
    for i in temp:
        if temp.count(i) > 1:
            string = string.replace(i, '')
    return string