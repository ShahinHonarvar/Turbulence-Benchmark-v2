def insert_before_character(text):
    position = text.find('F')
    if position >= 0:
        return text[:position] + 'o' + text[position:]
    else:
        return text