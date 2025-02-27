def remove_repeat_chars(string):
    altered_string = ''
    for char in string:
        if string.count(char) == 1 or string.index(char) < 10 or string.index(char) > 76:
            altered_string += char
    return altered_string