def return_n_greatest_chars(value):
    result_set = sorted(value, key=ord, reverse=True)[0:14]
    return sorted(result_set)