def insert_after_character(s):
    return ''.join([ch + 'v' if ch == 'j' else ch for ch in s])