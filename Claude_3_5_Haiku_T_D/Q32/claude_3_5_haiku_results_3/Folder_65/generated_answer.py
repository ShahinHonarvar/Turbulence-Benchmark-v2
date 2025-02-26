def insert_after_character(string):
    result = []
    for char in string:
        result.append(char)
        if char == '6':
            result.append('9')
    return ''.join(result)