def return_n_greatest_chars(string):
    return sorted(sorted(string, reverse=True)[:80])