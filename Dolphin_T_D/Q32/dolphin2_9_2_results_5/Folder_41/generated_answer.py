def insert_after_character(s):
    return ''.join(('O' + s[i] if s[i] == 'O' and i + 1 < len(s) and (s[i + 1] != 'o') else s[i] for i in range(len(s))))