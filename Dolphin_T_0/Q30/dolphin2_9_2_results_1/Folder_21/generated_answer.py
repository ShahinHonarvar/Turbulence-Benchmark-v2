def insert_before_character(string):
    return 'K '.join([word if not word.endswith(' ') else word + 'K' for word in string.split(' ')])