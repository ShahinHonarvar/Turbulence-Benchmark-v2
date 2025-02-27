def insert_after_character(word):
    new_word = ''
    for i in word:
        if i == 'u':
            new_word += i + 'u'
        else:
            new_word += i
    return new_word