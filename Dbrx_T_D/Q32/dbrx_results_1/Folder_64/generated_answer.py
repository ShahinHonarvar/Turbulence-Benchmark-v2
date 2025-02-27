def insert_after_character(string):
    return string.replace('u', 'u' + 'u', 1).replace('uu', 'u', 1)