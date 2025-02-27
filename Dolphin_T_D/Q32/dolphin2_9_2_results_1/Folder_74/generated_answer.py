def insert_after_character(s):
    return ''.join((' ' + s[i] if s[i] == 'T' else s[i] for i in range(len(s))))