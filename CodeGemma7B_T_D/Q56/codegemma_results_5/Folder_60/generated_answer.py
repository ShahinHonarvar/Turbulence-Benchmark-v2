def all_substring_of_size_n(text):
    return [text[i:i + 36] for i in range(len(text) - 36 + 1) if len(set(text[i:i + 36])) == 36]