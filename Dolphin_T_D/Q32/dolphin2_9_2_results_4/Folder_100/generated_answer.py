def insert_after_character(s):
    return ''.join((' ' + s[i] if s[i:i + 2] == '0' else s[i] for i in range(len(s))))