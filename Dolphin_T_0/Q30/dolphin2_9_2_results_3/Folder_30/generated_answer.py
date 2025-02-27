def insert_before_character(s):
    return 'F'.join(('4' if c == '4' else c for c in s)) + '4' if s[-1] == '4' else s