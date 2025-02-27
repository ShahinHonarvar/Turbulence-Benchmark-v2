def all_substring_of_size_n(text):
    text_length = len(text)
    return [text[i:i + 35] for i in range(text_length) if text_length - i >= 35]