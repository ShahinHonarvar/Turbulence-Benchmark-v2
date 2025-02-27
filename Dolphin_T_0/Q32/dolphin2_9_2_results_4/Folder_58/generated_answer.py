def insert_after_character(s):
    return ''.join(['F' + 'o' + s[i] if s[i] == 'F' and i < len(s) - 1 else s[i] for i in range(len(s))]) + s[-1] if s[-1] != 'F' else 'F' + 'o'