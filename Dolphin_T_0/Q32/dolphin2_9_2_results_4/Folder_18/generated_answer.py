def insert_after_character(string):
    return ''.join(('l' if string[i] == 'K' and i != len(string) else string[i] for i in range(len(string))))