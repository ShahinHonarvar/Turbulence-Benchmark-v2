def return_n_greatest_chars(string_of_chars):
    return sorted(list(set(string_of_chars)), reverse=True)[:49]