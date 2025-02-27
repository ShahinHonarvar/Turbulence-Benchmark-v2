def insert_before_character(s):
    return 'G' + s if s[0] == 't' else s[0] + ('' if s[1:].find('t') == -1 else 'G' + s[1:s.find('t') + 1] + s[s.find('t') + 1:])