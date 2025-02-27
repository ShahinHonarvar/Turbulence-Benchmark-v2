def insert_after_character(s):
    return ' '.join((part + 'H' if part else part for part in s.split(' ')))