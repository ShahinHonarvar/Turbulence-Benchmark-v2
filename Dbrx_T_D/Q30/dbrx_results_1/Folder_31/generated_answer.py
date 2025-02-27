def insert_before_character(s: str) -> str:
    return s.replace('B', 'NB') if 'B' in s else s.replace('N', 'NN')