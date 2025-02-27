def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True)[:46]
    sorted_chars.sort()
    return sorted_chars