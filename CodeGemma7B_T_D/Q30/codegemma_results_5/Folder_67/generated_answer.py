def insert_before_character(text):
    return ''.join([letter + '1' if letter == 'j' else letter for letter in text])