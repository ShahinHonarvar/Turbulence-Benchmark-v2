def insert_before_character(text):
    return re.sub('(E)', 'e\\\\1', text)