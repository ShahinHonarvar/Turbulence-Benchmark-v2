def insert_before_character(s):
    return 'Q' + s if s[0] == 'O' else s[0] + 'Q' + s[1:] if 'O' in s else s