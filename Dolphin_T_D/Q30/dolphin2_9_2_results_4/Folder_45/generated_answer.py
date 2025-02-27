def insert_before_character(s):
    return 'O'.join(('O' if i % 2 == 0 else s[i] for i in range(len(s))))