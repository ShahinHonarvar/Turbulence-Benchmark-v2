def insert_before_character(s):
    return 'F'.join(('U' + s[i] if s[i] == 'U' and i > 0 else s[i] for i in range(len(s))))