def return_n_smallest_chars(text):
    return sorted([char for char in text], reverse=True)[:87]