def insert_before_character(str):
    response = str
    for char in str:
        if char == 'Y':
            response = response[:response.index(char)] + '4' + response[response.index(char):]
    return response