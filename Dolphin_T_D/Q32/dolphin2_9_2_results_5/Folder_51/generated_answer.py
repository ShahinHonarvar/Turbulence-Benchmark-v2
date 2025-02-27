def insert_after_character(string):
    return 'O'.join([s if s != 'o' else o + 'O' for s in string])