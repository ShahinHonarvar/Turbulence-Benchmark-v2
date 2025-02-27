def all_substring_of_size_n(text):
    return [text[i:i + 41] for i in range(len(text) - 41 + 1)]