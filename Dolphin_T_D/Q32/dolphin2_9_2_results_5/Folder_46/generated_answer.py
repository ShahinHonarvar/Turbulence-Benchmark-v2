def insert_after_character(text):
    return ''.join(('W' if i > 0 and text[i - 1] == '6' else text[i] for i in range(len(text))))