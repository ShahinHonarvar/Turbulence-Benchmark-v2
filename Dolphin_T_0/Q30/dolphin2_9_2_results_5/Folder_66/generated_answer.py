def insert_before_character(string):
    return 'k' + string if string[0] == 'k' else string[0] + insert_before_character(string[1:]) if string else ''