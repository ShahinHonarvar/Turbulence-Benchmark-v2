def insert_before_character(user_string):
    result = ''
    for char in user_string:
        if char == 'I':
            result += 'I'
        result += char
    return result