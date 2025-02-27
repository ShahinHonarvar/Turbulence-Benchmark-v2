def insert_after_character(string):
    new_string = ''
    for i in string:
        new_string += i + 'o' if i == ' ' else i
    return new_string