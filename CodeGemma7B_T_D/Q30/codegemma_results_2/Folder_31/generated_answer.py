def insert_before_character(input_string):
    output = []
    for char in input_string:
        if char == 'B':
            output.append('N')
        output.append(char)
    return ''.join(output)