def insert_after_character(s):
    return ''.join(('Uu' if i > 0 and s[i - 1] == 'U' else s[i] for i in range(len(s))))