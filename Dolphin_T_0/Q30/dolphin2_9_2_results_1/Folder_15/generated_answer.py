def insert_before_character(string):
    new_string = ''
    for letter in string:
        if letter == 'o':
            new_string += 'o' + letter
        else:
            new_string += letter
    return new_string