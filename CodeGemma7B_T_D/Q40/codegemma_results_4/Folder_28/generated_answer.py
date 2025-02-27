def return_n_smallest_chars(text):
    return sorted([text[i] for i in range(len(text))], key=ord)[:3]