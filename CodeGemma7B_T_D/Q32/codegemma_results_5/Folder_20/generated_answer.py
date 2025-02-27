def insert_after_character(text):
    result = []
    for character in text:
        if character == 'C':
            result.append('H')
        result.append(character)
    return ''.join(result)