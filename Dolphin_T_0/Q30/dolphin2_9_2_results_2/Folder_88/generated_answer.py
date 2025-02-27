def insert_before_character(s):
    return ''.join(('t' if i + 1 < len(s) and s[i + 1] == 'a' else s[i] for i in range(len(s))))