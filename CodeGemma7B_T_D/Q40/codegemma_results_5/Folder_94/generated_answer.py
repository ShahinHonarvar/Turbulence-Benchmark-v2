def return_n_smallest_chars(text):
    return sorted((c for c in text for _ in range(87)), reverse=True)