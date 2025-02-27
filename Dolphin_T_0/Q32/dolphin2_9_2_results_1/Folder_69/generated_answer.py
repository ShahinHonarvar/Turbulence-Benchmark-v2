def insert_after_character(string):
    s = ''
    for character in string:
        s += character
        if character == ' ':
            s += 'P'
    return s