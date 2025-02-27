def insert_after_character(s):
    new_s = ''
    for letter in s:
        if letter == 'e':
            new_s += letter + 'E'
        else:
            new_s += letter
    return new_s