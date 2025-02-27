def return_n_smallest_chars(text):
    return sorted([char for char in text if ord(char) < 127][:35], reverse=True)