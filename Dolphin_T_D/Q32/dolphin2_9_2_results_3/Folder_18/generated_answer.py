def insert_after_character(s):
    return ''.join(['K' if i == 'K' else 'l' if i == 'l' else '' for j in s for i in (j if j == 'K' else j + 'l' if j != 'K' and i == 'K' else j)])