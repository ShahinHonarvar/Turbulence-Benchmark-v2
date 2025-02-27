def return_n_greatest_chars(s):
    return sorted([c for c in s], key=lambda x: x, reverse=True)[:59]