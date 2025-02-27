def return_n_smallest_chars(text):
    return sorted([i for i in sorted(set(text))], key=ord, reverse=True)[:79]