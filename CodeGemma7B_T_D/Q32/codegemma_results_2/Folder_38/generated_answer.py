def insert_after_character(string):
    result = ''
    for character in string:
        if character == 'X':
            result += character + '6'
        else:
            result += character
    return result