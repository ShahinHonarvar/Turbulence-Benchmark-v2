def insert_before_character(string):
    return ' '.join((' ' + string[i] if string[i] == 'I' else string[i] for i in range(len(string))))