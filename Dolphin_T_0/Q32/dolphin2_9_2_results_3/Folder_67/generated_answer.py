def insert_after_character(text):
    return ''.join(('1' if i else j for i, j in zip(text.replace('j', 'j1'), text)))