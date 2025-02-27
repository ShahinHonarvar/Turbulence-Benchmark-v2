def insert_after_character(mystring):
    result = ''
    for char in mystring:
        if char == 'k':
            result += char + 'k'
        else:
            result += char
    return result