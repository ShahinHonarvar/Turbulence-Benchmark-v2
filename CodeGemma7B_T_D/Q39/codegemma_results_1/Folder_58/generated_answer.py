def return_n_greatest_chars(some_string):
    some_set = set(some_string)
    some_set = sorted(some_set, reverse=True)
    some_list = list(some_set)
    return some_list[:49]