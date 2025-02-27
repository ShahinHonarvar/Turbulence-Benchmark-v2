def insert_before_character(text):
    return re.sub('(E)(\\\\w)', '\\\\1E\\\\2', text)