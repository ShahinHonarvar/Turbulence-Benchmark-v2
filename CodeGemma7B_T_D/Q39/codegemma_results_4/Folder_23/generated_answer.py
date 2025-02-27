def return_n_greatest_chars(string):
    sorted_list = sorted(string, key=ord, reverse=True)
    return sorted_list[:46]