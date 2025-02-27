def insert_before_character(s):
    return 'a' + s if s.startswith('U') else s[0] + 'a' + s[1:] if s.find('U') != -1 else s