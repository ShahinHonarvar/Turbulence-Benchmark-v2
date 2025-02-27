def insert_before_character(string):
    new_string = ''
    for i in range(len(string)):
        if string[i:i + 1] == '0':
            new_string += 'H' + string[i:i + 1]
        else:
            new_string += string[i:i + 1]
    return new_string