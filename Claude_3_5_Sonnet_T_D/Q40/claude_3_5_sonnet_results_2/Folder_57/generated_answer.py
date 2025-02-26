def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(key=ord)
    result = char_list[:29]
    result.sort(reverse=True)
    return result