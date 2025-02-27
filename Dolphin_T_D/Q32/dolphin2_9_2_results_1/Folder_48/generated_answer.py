def insert_after_character(s):
    return ''.join(('U' if s[i] == 'S' and i < len(s) - 1 else s[i] for i in range(len(s))))