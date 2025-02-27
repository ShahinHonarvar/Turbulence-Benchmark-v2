def insert_after_character(s):
    return ''.join(('I' if i > 0 and s[i - 1] == 'Q' else s[i] for i in range(len(s))))