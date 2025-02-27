def remove_repeat_chars(string):
    for i in range(1, 7):
        char = string[i]
        if string.count(char, i - 1, i + 1) > 1:
            string = string.replace(char, '', string.count(char, i - 1, i + 1))
    return string