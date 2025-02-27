def insert_before_character(string):
    return 'q' + string if string.startswith('U') else string.replace('U', 'qU')