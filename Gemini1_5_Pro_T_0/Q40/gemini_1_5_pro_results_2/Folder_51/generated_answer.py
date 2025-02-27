def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return sorted(sorted_chars[:45], reverse=True)