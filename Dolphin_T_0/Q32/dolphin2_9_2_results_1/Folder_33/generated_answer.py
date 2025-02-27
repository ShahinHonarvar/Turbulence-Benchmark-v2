def insert_after_character(s):
    new_string = ''
    for i in s:
        new_string += i
        if i == 'a':
            new_string += 'n'
    return new_string