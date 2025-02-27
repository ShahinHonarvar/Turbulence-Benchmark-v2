def insert_after_character(string):
    return ''.join(('Z' if string[i] == 'C' else string[i] for i in range(len(string)))) + 'Z'