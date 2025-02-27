def insert_after_character(string):
    processed_string = []
    for char in string:
        if char == 'Y':
            processed_string.append(char)
            processed_string.append('4')
        else:
            processed_string.append(char)
    return ''.join(processed_string)