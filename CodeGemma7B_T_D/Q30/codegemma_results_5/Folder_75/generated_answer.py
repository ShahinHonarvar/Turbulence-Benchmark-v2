def insert_before_character(string):
    return ''.join([x + ('q' if x == 'U' else '') for x in string])