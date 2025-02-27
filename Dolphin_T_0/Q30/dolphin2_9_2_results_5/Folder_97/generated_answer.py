def insert_before_character(s):
    return ''.join(('h' if i + 1 < len(s) and s[i + 1] == 'o' else s[i] for i in range(len(s))))