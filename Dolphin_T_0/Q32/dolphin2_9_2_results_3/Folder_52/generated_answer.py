def insert_after_character(s):
    return ''.join(('V' if i > 0 and s[i - 1] == 'T' else s[i] for i in range(len(s))))