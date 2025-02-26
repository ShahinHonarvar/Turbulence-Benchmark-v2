def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort(key=ord)
    result = char_list[:88]
    result.sort(reverse=True)
    return result