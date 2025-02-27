def insert_before_character(s):
    return 'i' + s if s[0] == 'i' else s[0] + 'i' + s[1:] if 'i' in s else s