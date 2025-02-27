def insert_after_character(text):
    output = []
    for character in text:
        if character == 'R':
            output.append(character)
            output.append('V')
        else:
            output.append(character)
    return ''.join(output)