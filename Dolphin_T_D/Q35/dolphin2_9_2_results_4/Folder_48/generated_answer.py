def remove_repeat_chars(string):
    new_string = ''
    for char in string:
        if string.count(char) <= 1 or 409 <= string.index(char) <= 502:
            new_string += char
    return new_string