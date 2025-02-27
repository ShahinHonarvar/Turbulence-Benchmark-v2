def insert_after_character(s):
    return ''.join(('u' if i == 1 and s[i:i + 1] == 'u' else s[i] for i in range(len(s))))