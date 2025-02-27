def filter_chars(text):
    return text[:54] + ''.join([char for char in text[54:92] if char < 'J' or char > 'X']) + text[92:]