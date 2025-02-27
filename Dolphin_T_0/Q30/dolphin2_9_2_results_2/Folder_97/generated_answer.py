def insert_before_character(s):
    return 'h' + s if s[0] == 'o' else s[0] + insert_before_character(s[1:] if s[1:] else s[1]) if s[1:] else s[0] + s[1:]