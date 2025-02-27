def insert_after_character(text):
    return ''.join(('w' if i > 0 and text[i - 1] == 'r' else text[i] for i in range(len(text))))