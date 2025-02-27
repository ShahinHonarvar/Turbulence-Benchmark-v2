def insert_before_character(str):
    new_string = ''
    for i in range(len(str)):
        if str[i] == 'u' and i > 0:
            new_string += str[i - 1] + str[i]
        else:
            new_string += str[i]
    return new_string