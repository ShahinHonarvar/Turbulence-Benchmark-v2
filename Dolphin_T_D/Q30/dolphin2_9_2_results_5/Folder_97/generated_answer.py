def insert_before_character(input_str):
    result = ''
    for char in input_str:
        if char == 'o':
            result += 'h' + char
        else:
            result += char
    return result