def insert_before_character(s):
    return ''.join(('z' if s[i] == 'N' else s[i] for i in range(len(s))))