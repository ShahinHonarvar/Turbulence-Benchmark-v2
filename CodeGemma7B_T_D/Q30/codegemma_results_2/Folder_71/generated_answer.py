def insert_before_character(str_to_change):
    result_str = ''
    for char in str_to_change:
        if char == '2':
            result_str += 'S' + char
        else:
            result_str += char
    return result_str