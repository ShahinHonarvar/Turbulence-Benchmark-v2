def insert_before_character(text):
    return ''.join([char + ('M' if char == '9' else '') for char in text])