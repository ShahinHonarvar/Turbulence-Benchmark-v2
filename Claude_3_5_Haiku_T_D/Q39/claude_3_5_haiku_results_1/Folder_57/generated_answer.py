def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string), reverse=True)[:29]
    return sorted_chars