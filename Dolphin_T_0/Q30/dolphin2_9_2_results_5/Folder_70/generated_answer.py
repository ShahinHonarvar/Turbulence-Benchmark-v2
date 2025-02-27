def insert_before_character(string):
    return 'V'.join(('P' if c == 'P' else str(c) for c in string)) + 'P'[string[-1] == 'P']