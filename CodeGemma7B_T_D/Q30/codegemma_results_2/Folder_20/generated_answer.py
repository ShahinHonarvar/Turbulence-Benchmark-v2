def insert_before_character(word):
    new_word = []
    for i in range(len(word)):
        if word[i] == 'C':
            new_word.append('H')
        new_word.append(word[i])
    return ''.join(new_word)