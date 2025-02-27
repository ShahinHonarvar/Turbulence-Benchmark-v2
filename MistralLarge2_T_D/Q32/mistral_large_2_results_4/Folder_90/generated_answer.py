def insert_after_character(s):
    return ''.join((ch + ('F' if ch == 'U' else '') for ch in s))