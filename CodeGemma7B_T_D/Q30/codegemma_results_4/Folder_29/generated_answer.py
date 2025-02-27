def insert_before_character(word):
    for char in word:
        if char == 'N':
            word = word[:word.index(char)] + 'z' + word[word.index(char):]
    return word