def insert_before_character(s):
    output = ''
    for char in s:
        if char == '6':
            output += '9' + char
        else:
            output += char
    return output