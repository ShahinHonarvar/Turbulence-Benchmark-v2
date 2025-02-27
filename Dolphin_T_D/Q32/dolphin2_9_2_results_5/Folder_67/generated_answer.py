def insert_after_character(s):
    return ''.join(('1' if i > 0 and s[i - 1] == 'j' else s[i] for i in range(len(s))))