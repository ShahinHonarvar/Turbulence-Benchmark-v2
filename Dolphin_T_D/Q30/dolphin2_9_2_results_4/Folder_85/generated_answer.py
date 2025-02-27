def insert_before_character(s):
    return ''.join(('a' if i + 1 < len(s) and s[i + 1] == 'o' else s[i] for i in range(len(s)))) + ('a' if len(s) and s[-1] == 'o' else '')