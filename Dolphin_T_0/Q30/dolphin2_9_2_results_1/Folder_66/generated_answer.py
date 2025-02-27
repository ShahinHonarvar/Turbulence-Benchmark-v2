def insert_before_character(s):
    return 'k' + s if s.startswith('k') else s.replace('k', 'kkr', 1)