def remove_repeat_chars(string):
    for char in set(string[1:7]):
        if string[1:7].count(char) > 1:
            string = string[:1] + string[1:7].replace(char, '', 1) + string[7:]
    return string