def insert_before_character(s):
    return '0'.join('H' * s.count('0') + s.split('0'))