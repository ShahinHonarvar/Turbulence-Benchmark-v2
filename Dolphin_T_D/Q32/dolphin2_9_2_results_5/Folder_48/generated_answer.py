def insert_after_character(s):
    return ''.join(('U' if i > 0 and s[i - 1] == 'S' else s[i] for i in range(len(s))))