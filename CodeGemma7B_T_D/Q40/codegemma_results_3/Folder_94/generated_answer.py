def return_n_smallest_chars(str):
    list_of_chars = sorted(str, key=ord)[:87]
    list_of_chars.sort(reverse=True)
    return list_of_chars