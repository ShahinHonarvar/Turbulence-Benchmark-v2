def insert_after_character(word):
    output = ''
    for letter in word:
        if letter == 'a':
            output += letter + 'a'
        else:
            output += letter
    return output