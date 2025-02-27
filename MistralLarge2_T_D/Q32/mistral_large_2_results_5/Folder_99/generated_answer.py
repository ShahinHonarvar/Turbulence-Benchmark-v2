def insert_after_character(s):
    return ''.join((ch + ('W' if ch == 'a' else '') for ch in s))