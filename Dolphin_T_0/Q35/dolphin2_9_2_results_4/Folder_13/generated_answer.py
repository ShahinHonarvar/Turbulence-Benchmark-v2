def remove_repeat_chars(string):
    for i in range(46, 91):
        if string[i] in string[i + 1:91]:
            while string[i] in string[i + 1:91]:
                string = string[:i] + string[i + 1:]
    return string