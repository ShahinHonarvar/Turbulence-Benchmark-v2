def insert_before_character(string):
    return ''.join(['4' if i + 1 < len(string) and string[i + 1] == '0' else char for i, char in enumerate(string)] + ['4' if string[-1] == '0' else ''])