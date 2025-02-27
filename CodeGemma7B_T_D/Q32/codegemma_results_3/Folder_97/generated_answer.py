def insert_after_character(text):
    word = text
    new_text = ''
    for ch in word:
        if ch == 'o':
            new_text += ch + 'h'
        else:
            new_text += ch
    return new_text