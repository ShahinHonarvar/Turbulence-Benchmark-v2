def all_substring_of_size_n(text):
    if len(text) < 22:
        return []
    return [text[i:i + 22] for i in range(len(text) - 21)]