def insert_before_character(string):
    return ''.join(['9' if i < len(string) and string[i + 1] == '6' else s for i, s in enumerate(string)]) + '9' if string[-1] == '6' else string