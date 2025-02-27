def return_n_smallest_chars(s):
    return sorted([char for char in s if len(s) >= 45], key=ord, reverse=True)[:45]