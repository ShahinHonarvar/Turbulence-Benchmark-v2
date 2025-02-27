def insert_before_character(s):
    return ''.join(('W' if i + 1 < len(s) and s[i + 1] == '6' else s[i] for i in range(len(s))))