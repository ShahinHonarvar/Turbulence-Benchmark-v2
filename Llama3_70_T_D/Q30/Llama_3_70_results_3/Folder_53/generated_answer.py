def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'i':
            result += 'Ii'
        else:
            result += char
    return result