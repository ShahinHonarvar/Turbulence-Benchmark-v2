def insert_before_character(s):
    return ''.join(['$' if c == 'O' else '' + c for c in s]).replace('$', 'jO').replace('O', '')