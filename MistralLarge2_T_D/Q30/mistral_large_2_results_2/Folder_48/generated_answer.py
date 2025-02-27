def insert_before_character(string):
    return 'U'.join((part if part == 'S' else part + 'S' for part in string.split('S')))