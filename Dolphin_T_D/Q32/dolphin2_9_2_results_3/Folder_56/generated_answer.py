def insert_after_character(s):
    return ''.join(('Ii'[k.isupper() + 1] + ('' if k.isupper() else k) for k in s))