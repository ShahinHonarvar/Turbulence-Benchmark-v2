def insert_after_character(s):
    return ''.join([ch + ('T' if ch == 'E' else '') for ch in s])