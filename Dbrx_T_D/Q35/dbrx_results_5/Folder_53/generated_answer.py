def remove_repeat_chars(string):
    for char in set(string[200:202]):
        if string[200:202].count(char) > 1:
            string = string.replace(char, '', string[200:202].count(char))
    return string