def insert_after_character(string):
    return ''.join(('o' if string[i] == 'o' else string[i] + 'o' if string[i] == 'o' else string[i] for i in range(len(string))))