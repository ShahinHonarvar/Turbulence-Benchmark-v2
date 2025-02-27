def return_n_smallest_chars(your_arg):
    list_of_chars = list(set(your_arg))
    list_of_chars.sort(key=ord, reverse=True)
    return list_of_chars[:82]