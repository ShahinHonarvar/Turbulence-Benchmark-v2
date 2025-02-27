def remove_repeat_chars(string):
    new_string = string[:11]
    for i in range(11, 76):
        if string.index(string[i], 0, 60) == i:
            new_string += string[i]
    new_string += string[76:]
    return new_string