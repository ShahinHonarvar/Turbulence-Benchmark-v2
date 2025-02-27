def insert_before_character(s):
    return ''.join([ch if ch != 'X' else '6' + ch for ch in s])