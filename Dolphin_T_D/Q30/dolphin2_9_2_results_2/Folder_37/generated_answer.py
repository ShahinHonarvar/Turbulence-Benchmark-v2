def insert_before_character(s):
    return 'a' + s if s.startswith('U') else s.replace('U', 'aU')