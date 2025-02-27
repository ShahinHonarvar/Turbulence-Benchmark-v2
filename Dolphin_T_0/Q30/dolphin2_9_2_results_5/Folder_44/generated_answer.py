def insert_before_character(s):
    return 'M' + s if s.startswith('g') else s.replace('g', 'Mg')