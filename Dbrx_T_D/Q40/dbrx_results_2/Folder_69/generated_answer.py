def return_n_smallest_chars(string_arg):
    list_result = sorted(list(string_arg), key=ord)[:65]
    list_result.sort(reverse=True)
    return list_result