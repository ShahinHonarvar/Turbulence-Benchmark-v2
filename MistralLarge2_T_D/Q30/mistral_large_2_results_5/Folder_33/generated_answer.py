def insert_before_character(s):
    return 'n'.join([char if char == 'a' else char + 'n' for char in s]).replace('nn', 'n')