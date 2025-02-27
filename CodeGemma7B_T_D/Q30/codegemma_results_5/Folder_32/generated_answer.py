def insert_before_character(str):
    return re.sub('(u)(F)', '\\\\2\\\\1', str)