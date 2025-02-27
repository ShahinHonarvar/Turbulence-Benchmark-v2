def insert_after_character(s):
    return ''.join(('R' if i > 0 and s[i - 1] == '5' else s[i] for i in range(len(s))))