def insert_after_character(s):
    return 'f'.join(('M' + s[i:i + 1] if s[i:i + 1] == 'M' else s[i:i + 1] for i in range(len(s))))