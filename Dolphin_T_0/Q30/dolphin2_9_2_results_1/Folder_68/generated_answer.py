def insert_before_character(s):
    return ''.join(('0' + s[i] if s[i] == 'i' else s[i] for i in range(len(s))))