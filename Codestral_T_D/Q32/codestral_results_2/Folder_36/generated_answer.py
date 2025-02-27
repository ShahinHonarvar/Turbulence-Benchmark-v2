def insert_after_character(s):
    output = ''
    for char in s:
        output += char
        if char == 'A':
            output += 'H'
    return output