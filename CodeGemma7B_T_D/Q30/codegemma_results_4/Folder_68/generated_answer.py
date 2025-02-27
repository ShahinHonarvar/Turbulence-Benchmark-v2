def insert_before_character(string):
    for char in string:
        if char == 'i':
            string = string[:string.index(char)] + '0' + string[string.index(char):]
    return string