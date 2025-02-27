def insert_after_character(string):
    return ''.join(('f' if string[i] == 'E' and i != len(string) - 1 else string[i] for i in range(len(string))))