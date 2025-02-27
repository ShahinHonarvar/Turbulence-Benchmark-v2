def insert_after_character(s):
    return ''.join(('N' if prev == 'm' else ch for ch, prev in zip(' ' + s, s)))