def insert_after_character(string):
    return ''.join(['f' if i + 1 < len(string) and string[i] == 'M' and (string[i + 1] != 'f') else string[i] for i in range(len(string))])