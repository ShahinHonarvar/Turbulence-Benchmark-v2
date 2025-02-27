def remove_repeat_chars(string):
    for index, char in enumerate(string[18:60]):
        if string[index + 18:60].count(char) > 1:
            string = string[:index + 18] + string[index + 18 + string[index + 18:60].index(char) + 1:]
    return string