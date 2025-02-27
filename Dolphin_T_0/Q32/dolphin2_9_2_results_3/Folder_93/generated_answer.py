def insert_after_character(s):
    return ''.join(['4' if s[i:i + 2] == 'Y\n' else s[i:i + 2] for i in range(0, len(s), 2)])