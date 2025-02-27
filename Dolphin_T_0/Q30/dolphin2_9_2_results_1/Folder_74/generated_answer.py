def insert_before_character(s):
    return ' '.join((' ' + s[i] + s[i + 1:] if s[i] == 'T' else s[i] + s[i + 1:] for i in range(len(s))))