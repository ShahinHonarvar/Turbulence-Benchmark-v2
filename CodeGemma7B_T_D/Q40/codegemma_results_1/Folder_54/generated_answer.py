def return_n_smallest_chars(str):
    list_of_char = list(str)
    list_of_char.sort(key=ord, reverse=True)
    return list_of_char[:79]