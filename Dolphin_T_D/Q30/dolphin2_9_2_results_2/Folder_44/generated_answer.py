def insert_before_character(s):
    return 'M' + s if s.startswith('g') else s[:1] + 'M' + s[1:] if 'g' in s else s