def return_n_smallest_chars(str):
    output = sorted(str, key=ord, reverse=True)
    return output[:9]