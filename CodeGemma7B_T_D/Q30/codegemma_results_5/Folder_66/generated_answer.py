def insert_before_character(arg):
    output = ''
    for char in arg:
        if char == 'k':
            output = output + 'k'
        output = output + char
    return output