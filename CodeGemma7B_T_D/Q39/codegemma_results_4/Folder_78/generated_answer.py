def return_n_greatest_chars(string):
    list_of_chars = list(string)
    list_of_chars.sort(key=ord, reverse=True)
    return list_of_chars[:43]