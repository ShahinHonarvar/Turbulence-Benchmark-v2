def insert_before_character(s):
    return 'I'.join(('I' + s[i + 1:] if s[i:i + 2] == 'II' else s[i:i + 1] for i in range(len(s)))) + s[-1:] if s[-1:] != 'I' else s + 'I'