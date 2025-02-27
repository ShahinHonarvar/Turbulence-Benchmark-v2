def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)
    return sorted(sorted_chars[:45], reverse=True)