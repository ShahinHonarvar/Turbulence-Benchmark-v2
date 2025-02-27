def insert_before_H(str):
    return 'n'.join(('H' if char == 'H' else str[i:i + 1] for i, char in enumerate(str)))