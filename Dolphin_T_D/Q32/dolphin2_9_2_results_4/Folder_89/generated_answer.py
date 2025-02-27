def insert_after_character(string):
    return 'W'.join([string[i] if string[i] != ' ' or string[i + 1] == ' ' else string[i] + 'W' for i in range(len(string))])