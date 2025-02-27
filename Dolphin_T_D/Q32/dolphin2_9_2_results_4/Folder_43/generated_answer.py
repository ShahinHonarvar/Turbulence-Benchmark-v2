def insert_after_character(s):
    return ''.join(['G' if i % 2 == 0 and s[i:i + 2] == 'th' else s[i] for i in range(len(s))]) + s[-1:]