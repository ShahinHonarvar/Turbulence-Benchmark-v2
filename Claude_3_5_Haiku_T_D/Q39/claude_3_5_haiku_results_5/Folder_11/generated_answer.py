def return_n_greatest_chars(string):
    sorted_chars = sorted(list(string), reverse=True)[:17]
    return sorted(sorted_chars)