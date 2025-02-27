def insert_before_character(s):
    return ''.join(['F' if i + 1 == s.find('4', i + 1) else c for i, c in enumerate(s)])