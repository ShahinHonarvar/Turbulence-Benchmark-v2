def insert_after_character(s):
    return ''.join(('9' if i > 0 and s[i - 1] == '6' else s[i] for i in range(len(s)))) + '9' if s[-1] == '6' else ''