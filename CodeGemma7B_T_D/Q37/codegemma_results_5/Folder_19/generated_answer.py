def filter_chars(text):
    filtered_text = ''.join([char for char in text if not (35 <= text.index(char) <= 89 and char >= 'E' and (char <= 't'))])
    return filtered_text