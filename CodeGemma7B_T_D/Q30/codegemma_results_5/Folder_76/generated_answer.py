def insert_before_character(str):
    return ''.join((ch + 'm' if ch == 'F' else ch for ch in str))