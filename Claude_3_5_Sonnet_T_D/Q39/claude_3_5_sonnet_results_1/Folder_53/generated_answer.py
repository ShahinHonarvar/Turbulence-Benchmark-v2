def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string), reverse=True)
    return sorted(sorted_chars[:19])