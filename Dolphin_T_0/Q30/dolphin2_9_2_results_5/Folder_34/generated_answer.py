def insert_before_character(s):
    return 'a' + s if s[0] == 'A' else s[0] + 'a' + s[1:] if 'A' in s else s