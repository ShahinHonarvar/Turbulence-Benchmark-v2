def return_n_greatest_chars(string):
    return sorted(list(set(string)), reverse=True)[:59]