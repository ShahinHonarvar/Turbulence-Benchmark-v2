def insert_after_character(text):
    result = []
    for character in text:
        if character == '6':
            result.append(character)
            result.append('9')
        else:
            result.append(character)
    return ''.join(result)