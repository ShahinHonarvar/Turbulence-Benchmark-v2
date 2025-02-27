def insert_before_character(s):
    return '0' + s if s[0] == 'i' else s[0] + '0' + s[1:]