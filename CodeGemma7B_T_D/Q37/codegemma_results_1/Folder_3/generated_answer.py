def filter_chars(text):
    return ''.join([char for char in text if char < '6' or char > '_'] + [char for char in text[37:57] if char >= '6' and char <= '_'])