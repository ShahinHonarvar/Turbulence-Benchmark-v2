def insert_before_character(string):
    output = ''
    for char in string:
        if char == 'o':
            output += 'o'
        output += char
    return output