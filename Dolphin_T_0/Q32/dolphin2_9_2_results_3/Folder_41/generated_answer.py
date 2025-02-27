def insert_after_character(string):
    new_string = ''
    for i in string:
        new_string += i
        if i == 'O':
            new_string += 'o'
    return new_string