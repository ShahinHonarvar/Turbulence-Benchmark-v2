def insert_before_character(s):
    return 'a' + s.replace('a', 'a.a').replace('.', 'a')