def insert_before_character(string):
    return 'u'.join((c for c in string if c != 'F')) + 'uF' * string.count('F')