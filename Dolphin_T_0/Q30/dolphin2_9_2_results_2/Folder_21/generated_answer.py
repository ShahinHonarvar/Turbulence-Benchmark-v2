def insert_before_character(text):
    return 'K '.join([word if word.endswith(' ') else word + 'K ' for word in text.split(' ')])