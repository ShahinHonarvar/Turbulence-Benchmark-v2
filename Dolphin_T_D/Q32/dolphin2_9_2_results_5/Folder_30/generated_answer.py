def insert_after_character(string):
    output = ''
    for char in string:
        output += char
        if char == '4':
            output += 'F'
    return output