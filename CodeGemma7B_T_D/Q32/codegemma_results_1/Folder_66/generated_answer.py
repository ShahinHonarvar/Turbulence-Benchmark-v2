def insert_after_character(text):
    characters = list(text)
    index = 0
    while index < len(characters):
        if characters[index] == 'k':
            characters.insert(index + 1, 'k')
            index += 2
        else:
            index += 1
    return ''.join(characters)