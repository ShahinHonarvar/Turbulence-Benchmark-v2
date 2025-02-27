def insert_before_character(s):
    return 'n' + s if s == 'a' else s[0] + 'n' + s[1:] if s[0] == 'a' else s[0] + insert_before_character(s[1:])