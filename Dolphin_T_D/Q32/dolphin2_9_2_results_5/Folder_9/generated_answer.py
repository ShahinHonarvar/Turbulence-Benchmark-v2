def insert_after_character(s):
    return 'E'.join([ch + ('E' if ch == 'e' else '') for ch in s])