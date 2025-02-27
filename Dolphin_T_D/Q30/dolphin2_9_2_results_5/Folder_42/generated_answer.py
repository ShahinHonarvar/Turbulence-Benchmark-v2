def insert_before_character(s):
    return ''.join(['j' if i == 'O' else c for c in s]).replace('O', 'jO')