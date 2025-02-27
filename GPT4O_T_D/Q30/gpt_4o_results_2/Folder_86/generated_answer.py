def insert_before_character(s):
    return ''.join(('QO' if s[i] == 'O' else s[i] for i in range(len(s))))