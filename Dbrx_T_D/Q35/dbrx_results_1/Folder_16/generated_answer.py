def remove_repeat_chars(string):
    for char in string:
        if string[89:97].count(char) > 1:
            string = string.replace(char, '', string[89:97].index(char))
    return string