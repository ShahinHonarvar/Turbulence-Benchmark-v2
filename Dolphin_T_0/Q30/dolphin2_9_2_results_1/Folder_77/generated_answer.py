def insert_before_character(my_string):
    new_string = ''
    for i in my_string:
        if i == '9':
            new_string += 'h9'
        else:
            new_string += i
    return new_string