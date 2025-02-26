def return_n_greatest_chars(string):
    sorted_chars = sorted(list(string), reverse=True)[:5]
    return sorted(sorted_chars)