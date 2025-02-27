def insert_after_character(s):
    return ''.join(('9' if i == 6 else str(i) for i in s))