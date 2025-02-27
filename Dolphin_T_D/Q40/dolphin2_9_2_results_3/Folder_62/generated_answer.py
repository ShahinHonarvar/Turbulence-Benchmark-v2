def return_n_smallest_chars(string):
    string_list = list(string)
    sorted_string_list = sorted(string_list, key=lambda c: ord(c))
    return_list = sorted_string_list[:84]
    return_list.sort(reverse=True)
    return return_list