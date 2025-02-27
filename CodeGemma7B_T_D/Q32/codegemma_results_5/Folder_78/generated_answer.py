def insert_after_character(arg):
    output = ''.join([i + ('s' if i == 'H' else '') for i in arg])
    return output