def return_n_greatest_chars(given_string):
    list_of_chars = list(given_string)
    list_of_chars.sort(key=ord)
    return list_of_chars[-52:]