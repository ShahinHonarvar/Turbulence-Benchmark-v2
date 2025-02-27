def insert_before_character(s):
    return '0'.join(('e' if c == 'e' else '' + s[i:i + 1] for i in range(len(s))))