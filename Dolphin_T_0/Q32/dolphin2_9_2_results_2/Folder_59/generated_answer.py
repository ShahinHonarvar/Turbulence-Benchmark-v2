def insert_after_character(my_string):
    result = ''
    for char in my_string:
        result += char
        if char == 'o':
            result += '0'
    return result