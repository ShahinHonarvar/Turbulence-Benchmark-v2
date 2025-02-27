def remove_repeat_chars(string):
    for char in string[22:24]:
        if string[22:24].count(char) > 1:
            string = string.replace(char, '', string[22:24].count(char))
    return string