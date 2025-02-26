def return_n_greatest_chars(string):
    return sorted(set(string), reverse=True)[:56]