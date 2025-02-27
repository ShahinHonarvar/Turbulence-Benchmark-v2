def insert_after_character(s):
    return ''.join(('Q' if i > 0 and s[i - 1] == 'O' and (s[i] != 'Q') else s[i] for i in range(len(s))))