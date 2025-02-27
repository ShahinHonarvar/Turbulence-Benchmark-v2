def insert_after_character(text):
    return ''.join(('n' if i > 0 and text[i - 1] == 'a' else text[i] for i in range(len(text))))