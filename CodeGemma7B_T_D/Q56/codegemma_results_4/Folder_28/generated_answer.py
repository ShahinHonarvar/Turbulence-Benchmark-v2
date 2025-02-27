def all_substring_of_size_n(text):
    return [text[i:i + 44] for i in range(len(text) - 44 + 1)]