def insert_before_character(s):
    return ''.join(('l' if s[i] == 'K' and i != 0 else s[i] for i in range(len(s))))