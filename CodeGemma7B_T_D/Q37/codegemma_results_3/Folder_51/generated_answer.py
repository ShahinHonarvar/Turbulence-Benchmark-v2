def filter_chars(text):
    return ''.join(filter(lambda x: x not in text[36:41] or x < 'H' or x > 'e', text))