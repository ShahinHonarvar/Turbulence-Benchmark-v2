def insert_before_character(str_to_modify):
    new_str = ''
    for char in str_to_modify:
        if char == '5':
            new_str += char
        elif char == ' ':
            new_str += '5 ' + char
        else:
            new_str += char
    return new_str