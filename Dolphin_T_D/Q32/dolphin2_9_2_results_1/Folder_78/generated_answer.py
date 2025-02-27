def insert_after_character(string):
    return ''.join(('s' if i and string[i - 1] == 'H' else string[i] for i in range(len(string) + 1)))