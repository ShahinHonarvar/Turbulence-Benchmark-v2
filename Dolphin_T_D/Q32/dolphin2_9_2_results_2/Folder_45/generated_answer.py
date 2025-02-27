def insert_after_character(s):
    if not s:
        return s
    else:
        return s[0] + 'O' + insert_after_character(s[1:]) if s[0] == 'O' else s[0] + insert_after_character(s[1:])