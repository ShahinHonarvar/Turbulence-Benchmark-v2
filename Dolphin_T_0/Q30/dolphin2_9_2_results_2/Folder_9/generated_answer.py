def insert_before_character(s):
    return ''.join(('E' + s[i] if s[i] == 'e' and i != 0 else s[i] for i in range(len(s))))