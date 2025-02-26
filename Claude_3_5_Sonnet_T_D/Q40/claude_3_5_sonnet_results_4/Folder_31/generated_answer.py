def return_n_smallest_chars(string):
    char_list = list(set(string))
    char_list.sort(key=ord)
    result = char_list[:70]
    result.sort(reverse=True)
    return result