def insert_after_character(input_string):
    result = input_string.replace('x', 'xN')
    return result.replace('xN', 'Nx', 1) if 'xN' in result else result