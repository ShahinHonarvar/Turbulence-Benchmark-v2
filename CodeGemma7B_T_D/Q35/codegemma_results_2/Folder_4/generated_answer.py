def remove_repeat_chars(text):
    filtered_text = ''.join([char for char in text if text.index(char) not in range(49, 74)])
    return filtered_text