def insert_after_character(string):
    return ''.join(['0' if string[i] == 'e' and i != 0 else string[i] for i in range(len(string))])