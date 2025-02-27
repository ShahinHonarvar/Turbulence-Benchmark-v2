def insert_after_character(text):
    return ''.join(list(('o' if i > 0 and text[i - 1] == 'F' else text[i] for i in range(len(text)))))