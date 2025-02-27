def insert_after_character(s):
    return ''.join(('0' if prev == 'i' else x for prev, x in zip(s, s[1:]))) + s[-1]