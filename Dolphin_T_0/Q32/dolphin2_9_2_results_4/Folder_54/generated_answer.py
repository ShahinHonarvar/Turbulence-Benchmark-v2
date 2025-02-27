def insert_after_character(s):
    return ''.join(('f' if i == len(s) - 1 and s[i] == 'M' else s[i] if s[i - 1] != 'M' or s[i] != 'M' else 'f' + s[i] for i in range(len(s))))