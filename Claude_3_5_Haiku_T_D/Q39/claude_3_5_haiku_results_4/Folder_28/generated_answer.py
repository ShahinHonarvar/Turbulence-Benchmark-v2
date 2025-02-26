def return_n_greatest_chars(string):
    sorted_chars = sorted(list(set(string)), reverse=True)[:3]
    return sorted(sorted_chars)