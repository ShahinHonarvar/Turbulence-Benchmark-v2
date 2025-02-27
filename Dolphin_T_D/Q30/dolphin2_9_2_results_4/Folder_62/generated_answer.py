def insert_before_character(s):
    return 'o' + s if s[0] == ' ' else s[0] + 'o' + s[1:] if ' ' in s else s