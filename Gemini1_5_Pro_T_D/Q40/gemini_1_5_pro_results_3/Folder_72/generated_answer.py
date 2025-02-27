def return_n_smallest_chars(string):
    sorted_chars = sorted(list(string), key=ord)
    return sorted(sorted_chars[:37], key=ord, reverse=True)