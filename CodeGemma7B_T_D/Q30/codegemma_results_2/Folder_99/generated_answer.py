def insert_before_character(str1):
    output = ''
    for char in str1:
        if char == 'a':
            output += 'W' + char
        else:
            output += char
    return output