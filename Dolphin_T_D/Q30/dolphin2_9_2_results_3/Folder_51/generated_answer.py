def insert_before_character(s):
    return 'O' + s if s[0] == 'o' else s[0] + 'O' + s[1:] if 'o' in s else s