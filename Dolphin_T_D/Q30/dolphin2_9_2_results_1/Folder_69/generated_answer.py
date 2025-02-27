def insert_before_character(s):
    return 'P' + s if s[0] == ' ' else s[0] + 'P' + s[1:] if ' ' in s else s