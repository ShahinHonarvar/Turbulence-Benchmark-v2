def insert_after_character(s):
    return ''.join(('u' if i > 0 and s[i - 1] == 't' else '' + s[i] for i in range(len(s))))