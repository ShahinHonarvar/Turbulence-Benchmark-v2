def insert_before_character(string):
    return ''.join([c + ('O' if c == 'O' else '') for c in string])