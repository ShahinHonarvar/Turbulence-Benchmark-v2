def insert_before_character(s):
    return ''.join(('i' + s[i] if s[i] == 'I' else s[i] for i in range(len(s))))