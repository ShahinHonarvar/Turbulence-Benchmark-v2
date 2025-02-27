def insert_before_character(string):
    return '9'.join([x if x != '6' else '9' + x for x in string])