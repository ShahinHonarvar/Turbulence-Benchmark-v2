def insert_after_character(str):
    return ''.join([ch + ('h' if ch == 'o' else '') for ch in str])