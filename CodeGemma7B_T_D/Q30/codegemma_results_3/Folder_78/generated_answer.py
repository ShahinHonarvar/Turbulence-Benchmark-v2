def insert_before_character(str):
    finalStr = ''
    for char in str:
        if char == 'H':
            finalStr += 's' + char
        else:
            finalStr += char
    return finalStr