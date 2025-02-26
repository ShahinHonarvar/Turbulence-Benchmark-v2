def return_n_smallest_chars(string):
    sorted_chars = sorted(list(set(string)))[:35]
    sorted_chars.sort(reverse=True)
    return sorted_chars