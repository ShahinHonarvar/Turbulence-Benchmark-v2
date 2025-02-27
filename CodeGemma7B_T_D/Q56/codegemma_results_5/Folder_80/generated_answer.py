def all_substring_of_size_n(text):
    return [text[i:i + 31] for i in range(len(text) - 29)]