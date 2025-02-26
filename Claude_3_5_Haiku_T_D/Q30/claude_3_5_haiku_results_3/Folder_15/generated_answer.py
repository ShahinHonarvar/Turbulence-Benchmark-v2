def insert_before_character(string):
    result = []
    for char in string:
        if char == 'o':
            result.append('o')
        result.append(char)
    return ''.join(result)