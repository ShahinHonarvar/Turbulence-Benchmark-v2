def insert_after_character(text):
    return ''.join(['f' if i > 0 and text[i - 1] == 'M' else '' + text[i] for i in range(len(text))])