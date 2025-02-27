def remove_repeat_chars(string):
    for char in set(string[20:93]):
        if string[20:93].count(char) > 1:
            string = string.replace(char, '', string[20:93].count(char))
    return string