def insert_before_character(s):
    return ''.join(['a' + ch if ch == 'o' else ch for ch in s])