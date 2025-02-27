def insert_before_character(s):
    return 'a' + s if s[0] == 'o' else s[0] + 'a' + s[1:] if 'o' in s else s