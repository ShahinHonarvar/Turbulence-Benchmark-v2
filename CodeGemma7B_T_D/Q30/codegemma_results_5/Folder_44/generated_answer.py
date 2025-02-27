def insert_before_character(text):
    return ''.join([char + ('M' if char == 'g' else '') for char in text])