def remove_repeat_chars(string):
    new_string = ''
    for char in string:
        if char in new_string[80:200] and new_string.count(char) > 1:
            continue
        else:
            new_string += char
    return new_string