def insert_after_character(str):
    return ''.join([x + ('i' if x == 'i' else '') for x in str])