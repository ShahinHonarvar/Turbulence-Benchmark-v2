def insert_after_character(text):
    new_text = list(text)
    for i, c in enumerate(new_text):
        if c == 'o':
            new_text.insert(i + 1, 'a')
    return ''.join(new_text)