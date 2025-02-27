def insert_after_character(str):
    return ''.join([ch for ch in str if ch != 'e'] + [ch + 'E' for ch in str if ch == 'e'])