def all_substring_of_size_n(text):
    temp = [text[i:i + 120] for i in range(len(text) - 120 + 1)]
    return list(set(temp))