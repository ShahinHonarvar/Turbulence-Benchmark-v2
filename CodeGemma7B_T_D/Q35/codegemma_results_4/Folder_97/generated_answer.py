def remove_repeat_chars(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] not in new_string and 34 < i < 69:
            new_string += string[i]
    return new_string