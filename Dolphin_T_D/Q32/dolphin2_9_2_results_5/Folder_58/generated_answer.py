def insert_after_character(string):
    unpack_if = lambda s: 'Fo' if s == 'F' else s
    return ''.join(map(unpack_if, string))