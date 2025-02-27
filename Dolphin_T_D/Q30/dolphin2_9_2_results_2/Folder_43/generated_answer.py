def insert_before_character(mystring):
    result = ''
    for char in mystring:
        if char == 't':
            result += 'G' + char
        else:
            result += char
    return result