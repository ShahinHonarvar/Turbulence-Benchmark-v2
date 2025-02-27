def all_substring_of_size_n(text):
    return sorted({text[i:i + 92] for i in range(len(text) - 92 + 1)})