def insert_before_character(s):
    return 't'.join((part if i % 2 == 0 else part.replace('g', 'tg') for i, part in enumerate(s.split('g'))))