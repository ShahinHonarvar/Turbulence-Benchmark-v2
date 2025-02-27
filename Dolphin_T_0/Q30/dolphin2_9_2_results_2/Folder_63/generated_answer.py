def insert_before_character(s):
    return 'R'.join(['5' if c == '5' else c for c in s.split('5')]) + ('' if s[-1] == '5' else '')