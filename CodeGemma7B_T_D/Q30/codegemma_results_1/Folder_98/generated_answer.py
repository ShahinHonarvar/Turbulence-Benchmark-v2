def insert_before_character(s):
    return ''.join([ch + ('u' if ch.isupper() else '') for ch in s])