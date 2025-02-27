def insert_before_character(text):
    characters = text.split()
    for character in characters:
        if character == 'c':
            characters.insert(characters.index(character), 'G')
    return ' '.join(characters)