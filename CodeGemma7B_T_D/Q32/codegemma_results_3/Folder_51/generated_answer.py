def insert_after_character(text):
    return re.sub('(o)([a-zA-Z\\\\s])', '\\\\1O\\\\2', text)