def return_n_smallest_chars(string):
    char_list = list(set(string))
    char_list.sort()
    result = char_list[:64]
    result.sort(reverse=True)
    return result