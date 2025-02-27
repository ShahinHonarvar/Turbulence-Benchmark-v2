def insert_after_character(text):
    return ''.join(('f' if prev == 'M' and curr == ' ' else curr for prev, curr in zip(text, text[1:] + ' ')))