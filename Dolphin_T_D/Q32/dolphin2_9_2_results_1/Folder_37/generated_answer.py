def insert_after_character(string):
    return ''.join(('a' if string[i] == 'U' and i != len(string) - 1 else string[i] for i in range(len(string))))