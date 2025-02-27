def insert_after_character(word):
    new_word = word
    for letter in new_word:
        if letter == 'a':
            new_word = new_word[:new_word.index(letter) + 1] + 'a' + new_word[new_word.index(letter) + 1:]
    return new_word