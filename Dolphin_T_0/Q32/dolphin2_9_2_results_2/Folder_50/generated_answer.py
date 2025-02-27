def insert_after_character(s):
    return ''.join(('u' if i == t + 1 else s[i] for i, t in enumerate(s) if s[t] == 't'))