def insert_before_character(s):
    return '5 ' if s == ' ' else '5' + s if s[0] == ' ' else s[0] + insert_before_character(s[1:])