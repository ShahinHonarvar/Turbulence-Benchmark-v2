def insert_after_character(s):
    return ''.join(['Y' + '4' + s[i] if s[i] == 'Y' else s[i] for i in range(len(s))])