def insert_before_character(text):
    return re.sub('(?<![I])I', 'I\\\\1', text)