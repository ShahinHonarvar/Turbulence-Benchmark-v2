def insert_after_character(string):
    return ''.join(('H' if i == len(string) - 1 and string[i] == 'A' else string[i] if string[i] != 'A' else string[i] + 'H' for i in range(len(string))))