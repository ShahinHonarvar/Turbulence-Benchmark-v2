def insert_before_character(s):
    return 'A' + s if s[0] == 'A' else s[0] + 'A' + s[1:]