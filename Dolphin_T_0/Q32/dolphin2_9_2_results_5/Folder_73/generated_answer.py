def insert_after_character(string):
    return ''.join(['RV' if string[i] == 'R' else string[i] for i in range(len(string))])