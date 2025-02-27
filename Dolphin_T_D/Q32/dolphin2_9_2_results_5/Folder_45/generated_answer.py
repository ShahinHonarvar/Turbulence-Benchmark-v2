def insert_after_character(string):
    return ''.join(['O' if string[i] == 'O' and i > 0 else string[i] for i in range(len(string))])