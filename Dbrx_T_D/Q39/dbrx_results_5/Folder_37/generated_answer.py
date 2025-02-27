def return_n_greatest_chars(string):
    sorted_list = sorted(set(string), reverse=True)
    return sorted_list[:26]