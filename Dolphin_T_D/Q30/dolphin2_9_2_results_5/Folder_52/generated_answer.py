def insert_before_character(s):
    return ''.join(['V' if s[i - 1] == 'T' else s[i] for i in range(1, len(s))]).replace('T', 'VT', 1)