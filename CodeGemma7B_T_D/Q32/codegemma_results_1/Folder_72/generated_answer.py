def insert_after_character(text):
    text_split = text.split()
    for i, word in enumerate(text_split):
        if 'O' in word:
            word = word.replace('O', 'dO')
        text_split[i] = word
    text_joined = ' '.join(text_split)
    return text_joined