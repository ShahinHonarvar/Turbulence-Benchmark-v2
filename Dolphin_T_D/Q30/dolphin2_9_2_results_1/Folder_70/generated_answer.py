def insert_before_character(s):
    return ''.join(('V' if i.prev == 'P' else i.out for i in (itertools.groupby(s) if isinstance(s, str) else (s,)) if i.out != 'P'))