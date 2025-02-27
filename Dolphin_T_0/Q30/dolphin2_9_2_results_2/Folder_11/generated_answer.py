def insert_before_character(string):
    return 't' + string if string[0] == 'g' else string[0] + insert_before_character(string[1:]) if string[1:] else string[0]