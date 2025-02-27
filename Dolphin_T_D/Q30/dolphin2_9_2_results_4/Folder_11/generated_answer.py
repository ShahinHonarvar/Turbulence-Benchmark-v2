def insert_before_character(my_string):
    result = ''
    for char in my_string:
        if char == 'g':
            result += 't' + char
        else:
            result += char
    return result