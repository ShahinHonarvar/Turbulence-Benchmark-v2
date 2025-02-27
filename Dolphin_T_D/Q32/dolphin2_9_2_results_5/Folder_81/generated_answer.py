def insert_after_character(s):
    return ''.join(['A' if i % 2 == 0 and s[i:i + 1] == 'A' else s[i] for i in range(len(s))])