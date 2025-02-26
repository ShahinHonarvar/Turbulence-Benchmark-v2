def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string), reverse=True)[:10]
    return sorted(sorted_chars)