def insert_after_character(string):
    output = ''
    for char in string:
        if char == 'r':
            output += char + 'w'
        else:
            output += char
    return output