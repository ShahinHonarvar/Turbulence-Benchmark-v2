def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'x':
            result += 'Nx'
        else:
            result += char
    return result