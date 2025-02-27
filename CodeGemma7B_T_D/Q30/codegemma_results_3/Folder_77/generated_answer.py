def insert_before_character(text):
    return ''.join((text[i] + 'h' if text[i] == '9' else text[i] for i in range(len(text))))