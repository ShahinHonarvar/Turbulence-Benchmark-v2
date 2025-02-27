def filter_chars(string):
    remove_chars = string[3:9]
    for char in remove_chars:
        while char in string:
            string = string.replace(char, '', 1)
    return string