def insert_after_character(text):
    separated = text.split('b')
    combined = []
    for word in separated:
        combined.append(word + 'y')
    return ''.join(combined)