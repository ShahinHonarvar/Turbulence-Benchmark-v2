def insert_before_character(s):
    return 'T' * s.count('U') + s.replace('U', '') + 'U' * s.count('U')