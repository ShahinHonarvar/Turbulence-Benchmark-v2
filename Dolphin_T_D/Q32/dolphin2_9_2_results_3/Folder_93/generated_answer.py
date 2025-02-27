def insert_after_character(string):
    return ''.join(['4' if string[i - 1] == 'Y' else string[i] for i in range(len(string))])