def remove_repeat_chars(string):
    altered_string = ''
    for char in string:
        if string.count(char) == 1 and (string.index(char) > 46 and string.index(char) < 91):
            altered_string += char
    return altered_string