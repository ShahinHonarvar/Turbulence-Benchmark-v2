def insert_after_character(s):
    return ' '.join(('0' if i > 0 and s[i - 1] == '0' else s[i] for i in range(len(s))))