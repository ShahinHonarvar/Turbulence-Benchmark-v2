def insert_after_character(string):
    return 'Q'.join([string[i] if string[i] != 'm' else string[i] + 'Q' for i in range(len(string))])