def insert_before_character(s):
    return 'h' + s if s.startswith('5') else s[0] + 'h' + s[1:] if '5' in s else s