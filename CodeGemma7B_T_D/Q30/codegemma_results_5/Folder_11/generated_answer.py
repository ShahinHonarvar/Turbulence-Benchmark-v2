def insert_before_character(word):
    for i, c in enumerate(word):
        if c == 'g':
            word = word[:i] + 't' + word[i:]
    return word