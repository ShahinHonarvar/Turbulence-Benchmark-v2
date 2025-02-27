def insert_after_character(s):
    return 'F'.join([i + ('' if i != '4' else 'F') for i in s])