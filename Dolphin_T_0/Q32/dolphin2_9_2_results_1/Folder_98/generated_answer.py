def insert_after_character(s):
    return ''.join(('U' + s[i] if s[i - 1] == 'U' and i > 0 else s[i] for i in range(len(s)))) + ('u' if s[-1] == 'U' else '')