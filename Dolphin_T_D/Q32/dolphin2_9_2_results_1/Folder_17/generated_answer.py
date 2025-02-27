def insert_after_character(s):
    return 'I'.join((a + 'I' * (a == 'Q') + (b + 'I' * (b == 'Q')) for a, b in zip(s, s[1:] + ' ')))