def insert_after_character(s):
    return ''.join(('4' if i > 0 and s[i - 1] == 'Y' else s[i] for i in range(len(s))))