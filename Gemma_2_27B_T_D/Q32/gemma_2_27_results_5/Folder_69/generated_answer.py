def insert_after_character(s):
    return ''.join(['P' + c if c == ' ' else c for c in s])