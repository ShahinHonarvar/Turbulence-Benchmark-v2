from re import sub

def insert_before_character(text):
    new_text = sub('w+', 'wn', text)
    return new_text