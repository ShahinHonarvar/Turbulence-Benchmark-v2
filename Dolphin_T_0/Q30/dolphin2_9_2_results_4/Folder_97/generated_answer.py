def insert_before_character(my_string):
    new_string = ''
    for i in my_string:
        if i == 'o':
            new_string += 'h' + i
        else:
            new_string += i
    return new_string