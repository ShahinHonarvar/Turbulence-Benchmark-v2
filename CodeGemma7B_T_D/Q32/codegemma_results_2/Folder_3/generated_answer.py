def insert_after_character(txt):
    return ''.join([ch for ch in txt if ch == '0'] + ['H'] + [ch for ch in txt if ch != '0'])