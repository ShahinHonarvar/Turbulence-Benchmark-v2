def insert_after_character(string):
    return ''.join(['G' if string[i - 1] == 'c' and i != 0 else string[i] for i in range(len(string))])