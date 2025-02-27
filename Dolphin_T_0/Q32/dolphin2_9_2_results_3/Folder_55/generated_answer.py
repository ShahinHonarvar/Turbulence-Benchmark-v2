def insert_after_character(mystr):
    new_str = ''
    for i in range(len(mystr)):
        new_str += mystr[i]
        if mystr[i] == 'u':
            new_str += 'U'
    return new_str