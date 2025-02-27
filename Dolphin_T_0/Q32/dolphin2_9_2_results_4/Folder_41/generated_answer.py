def insert_after_character(text):
    return ''.join(('o' if i > 0 and text[i - 1] == 'O' else text[i] for i in range(len(text))))