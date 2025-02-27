def insert_after_character(string):
    return ''.join(('U' if i == len(string) - 1 and string[i] == 'S' else '' if string[i] != 'S' else 'S' + 'U' for i in range(len(string))))