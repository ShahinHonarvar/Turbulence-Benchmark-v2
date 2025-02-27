def insert_before_character(a):
    new_a = ''
    for letter in a:
        if letter == 'o':
            new_a += 'O' + letter
        else:
            new_a += letter
    return new_a