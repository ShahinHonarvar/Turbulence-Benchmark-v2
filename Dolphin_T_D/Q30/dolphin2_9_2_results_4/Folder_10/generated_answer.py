def insert_before_character(string):
    return 'v' + string if string.startswith('j') else string.replace('j', 'vj')