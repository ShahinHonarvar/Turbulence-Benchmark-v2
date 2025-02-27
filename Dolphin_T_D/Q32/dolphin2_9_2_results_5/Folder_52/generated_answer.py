def insert_after_character(string):
    return ''.join(('V' if i > 0 and string[i - 1] == 'T' else string[i] for i in range(len(string)))) + 'V' if len(string) > 0 and string[-1] == 'T' else ''