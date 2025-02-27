def insert_after_character(string):
    return ''.join(['N' if string[i:i + 2] == 'mm' else string[i] for i in range(len(string))])