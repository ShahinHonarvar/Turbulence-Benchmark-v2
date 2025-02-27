def insert_after_character(s):
    s = s.split('u')
    return 'u'.join([x + 'u' if len(x) != 0 else '' for x in s])