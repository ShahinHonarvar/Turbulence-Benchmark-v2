def insert_before_character(string):
    if string.find('U') == -1:
        return string
    new_string = string[:string.find('U')] + 'U' + string[string.find('U'):]
    return new_string