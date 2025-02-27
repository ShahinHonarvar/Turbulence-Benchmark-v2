def insert_before_character(string):
    new_string = ''
    for i in string:
        new_string += i
        if i == 'e':
            new_string += 'e'
    return new_string